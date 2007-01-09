%define __find_requires %{nil}
%define __find_provides %{nil}

Name: mathematica
Version: 5.2
Copyright: Commercial
Group: Applications/Scientific
Summary: Wolfram Mathematica 5.2
Release: 1
Packager: Rutgers University
Source: mathematica-5.2.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
From simple calculator operations to large-scale programming and
interactive-document preparation, Mathematica is the tool of choice at the
frontiers of scientific research, in engineering analysis and modeling, in
technical education from high school to graduate school, and wherever
quantitative methods are used.

%prep
%setup -q -n mathematica-5.2

%build
echo "Nothing to do"  # Nothing to do

%install
mkdir -p $RPM_BUILD_ROOT/usr/local
mkdir -p $RPM_BUILD_ROOT/usr/local/bin

cp -Rp Wolfram $RPM_BUILD_ROOT/usr/local

cd $RPM_BUILD_ROOT/usr/local/bin
for exe in MathKernel Mathematica math mathematica mcc; do
  ln -s ../Wolfram/Mathematica/5.2/Executables/${exe} .
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

You must obtain a license for Mathematica in order to have unrestricted use.
On inital startup, the license or license server will be requested.
Unlicensed copies of Mathematica will only operate in MathReader mode.

In order to use Mathematica remotely via X forwarding, you must run a
font server, serving the following font paths:
  /usr/local/Wolfram/Mathematica/5.2/SystemFiles/Fonts/BDF/
  /usr/local/Wolfram/Mathematica/5.2/SystemFiles/Fonts/Type1/
and the font path must be edited to obtain fonts from the font server.

EOF

%files
%defattr(-,root,bin)
/usr/local/Wolfram
/usr/local/bin/MathKernel
/usr/local/bin/Mathematica
/usr/local/bin/math
/usr/local/bin/mathematica
/usr/local/bin/mcc

