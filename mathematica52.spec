%define __find_requires %{nil}
%define __find_provides %{nil}

Name: mathematica
Version: 5.2
Copyright: Commercial
Group: Applications/Scientific
Summary: Wolfram Mathematica 5.2 and MathLM server
Release: 2
Packager: Rutgers University
Source0: mathematica-5.2.tar
BuildRoot: /var/tmp/%{name}-root

%description
From simple calculator operations to large-scale programming and
interactive-document preparation, Mathematica is the tool of choice at the
frontiers of scientific research, in engineering analysis and modeling, in
technical education from high school to graduate school, and wherever
quantitative methods are used.

This includes the MathLM server.

%prep
# To prepare the tarball, install Mathematica and MathLM.
# Create a directory mathematica-%{version} and copy the directory the
# installer puts down (Wolfram/...)
# Be sure to blank out any mathpass files
# Also grab the README and startup script from somewhere
%setup -q -n mathematica-5.2

%build
echo "Nothing to do"  # Nothing to do

%install
mkdir -p $RPM_BUILD_ROOT/usr/local
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
mkdir -p $RPM_BUILD_ROOT/etc/init.d

cp -Rp Wolfram $RPM_BUILD_ROOT/usr/local/
cp -p mathinfo $RPM_BUILD_ROOT/usr/local/Wolfram/MathLM/
cp -p mathlm $RPM_BUILD_ROOT/etc/init.d/
cp README $RPM_BUILD_ROOT/usr/local/Wolfram/README.Rutgers
cp fontserver $RPM_BUILD_ROOT/usr/local/Wolfram/

#cd $RPM_BUILD_ROOT/usr/local/bin
for exe in MathKernel Mathematica math mathematica mcc; do
  #ln -s ../Wolfram/Mathematica/5.2/Executables/${exe} .
  cp wrapper $RPM_BUILD_ROOT/usr/local/bin/${exe}
done

cd $RPM_BUILD_ROOT/usr/local/sbin
for exe in mathlm monitorlm; do
  ln -s ../Wolfram/MathLM/${exe} .
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

Read /usr/local/Wolfram/README.Rutgers information on setting up
Mathematica and MathLM.

EOF

%files
%defattr(-,root,bin)
/usr/local/Wolfram
/usr/local/bin/MathKernel
/usr/local/bin/Mathematica
/usr/local/bin/math
/usr/local/bin/mathematica
/usr/local/bin/mcc
/usr/local/sbin/mathlm
/usr/local/sbin/monitorlm
/etc/init.d/mathlm
%config(noreplace) /usr/local/Wolfram/Mathematica/5.2/Configuration/Licensing/mathpass
%config(noreplace) /usr/local/Wolfram/MathLM/mathpass
%config(noreplace) /usr/local/Wolfram/fontserver

