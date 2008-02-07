
Name: mathematica
Version: 6.0
Copyright: Commercial
Group: Applications/Scientific
Summary: Wolfram Mathematica 6 and MathLM server
Release: 3
Packager: Rutgers University
Source0: mathematica-%{version}.tar.gz
BuildRoot: /var/local/tmp/%{name}-root
AutoReq: 0
AutoProv: 0
#The above turn off the find-provides and find-requires dependency handler

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
%setup -q

%build
echo "Nothing to do"  # Nothing to do

%install
mkdir -p $RPM_BUILD_ROOT/usr/local
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
mkdir -p $RPM_BUILD_ROOT/etc/init.d

cp -Rp Wolfram $RPM_BUILD_ROOT/usr/local/
install -m 0755 mathlm $RPM_BUILD_ROOT/etc/init.d/
install -m 0644 README $RPM_BUILD_ROOT/usr/local/Wolfram/README.Rutgers
install -m 0644 fontserver $RPM_BUILD_ROOT/usr/local/Wolfram/

# We renamed mcc to mcc-mathetmatica to prevent conflicts with matlab's mcc
# Therefore we need to change the basename in the mcc-mathematica file to
# reflect this

for exe in MathKernel Mathematica math mathematica mcc-mathematica; do
  install -m 0755 wrapper $RPM_BUILD_ROOT/usr/local/bin/${exe}
done

cd $RPM_BUILD_ROOT/usr/local/bin/
mv mcc-mathematica mcc-mathematica.wrong
sed -e 's/\/usr\/bin\/basename/mcc/g' mcc-mathematica.wrong > mcc-mathematica
chmod 0755 mcc-mathematica

cd $RPM_BUILD_ROOT/usr/local/sbin
for exe in mathlm monitorlm; do
  ln -s ../Wolfram/MathLM/${exe} .
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

Setup:

   Read /usr/local/Wolfram/README.Rutgers for information on setting up
   Mathematica and MathLM

Installation Note:

   Normally, Mathematica's mcc can be run by simply typing mcc. However, due
   to possible conflicts with other licensed software (i.e. Matlab's mcc),
   /usr/local/bin/mcc has been renamed to /usr/local/bin/mcc-mathematica.
   You may want /usr/local/bin/mcc to be a script which informs the user of
   the new naming scheme (i.e. mcc-matlab and mcc-mathematica). If this
   conflict does not exist on your system you probably want to create the
   following link:
      ln -s /usr/local/bin/mcc-mathematica /usr/local/bin/mcc


EOF

%files
%defattr(-,root,bin)
/usr/local/Wolfram/Mathematica/%{version}/AddOns
/usr/local/Wolfram/Mathematica/%{version}/Documentation
/usr/local/Wolfram/Mathematica/%{version}/Executables
/usr/local/Wolfram/Mathematica/%{version}/SystemFiles
%config(noreplace) /usr/local/Wolfram/Mathematica/%{version}/Configuration/Licensing/mathpass
/usr/local/Wolfram/MathLM/SysAdminGuide.pdf
/usr/local/Wolfram/MathLM/mathinfo
/usr/local/Wolfram/MathLM/mathlm
/usr/local/Wolfram/MathLM/monitorlm
%config(noreplace) /usr/local/Wolfram/MathLM/mathpass
/usr/local/bin/MathKernel
/usr/local/bin/Mathematica
/usr/local/bin/math
/usr/local/bin/mathematica
/usr/local/bin/mcc-mathematica
/usr/local/sbin/mathlm
/usr/local/sbin/monitorlm
/etc/init.d/mathlm
%config(noreplace) /usr/local/Wolfram/fontserver

%changelog
* Tue Feb 5 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 6.0-3
- fixed permissions for mcc-mathematica
* Thu Jan 31 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 6.0-2
- renamed mcc to mcc-mathematica, changed basename to mcc in mcc wrapper, added install note
- added AutoReq and AutoProv instead of %define __find_requires %{null}, removed duplice file entries
