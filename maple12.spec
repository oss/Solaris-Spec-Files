#%define __find_requires %{nil}
#%define __find_provides %{nil}

Name: maple
Summary: Maple 12
Version: 12
Release: 2
Group: Licensed
Copyright: Licensed
Source0: maple%{version}.tar.gz
Source1: maple12.README.rutgers
Source2: maple12.init.d
# To build the maple11.tar.gz, go through the GUI maple installer and install
# maple and the network tools into /usr/local/maple11/{maple11,Network...}
# then run tar cf maple11.tar maple11 in /usr/local
BuildRoot: /var/local/tmp/%{name}-root
AutoReq: 0
AutoProv: 0
#The above disable the find_requires and find_provides dependency handlers


%description
Maple 12 is an essential tool for researchers, teachers, and students in any
technical discipline. It lets you explore, visualize, and solve even the most
complex mathematical problems, providing greater insight into the math and
reducing errors. Teachers can bring both simple and complex problems to life;
students can focus on concepts rather than the mechanics of solutions; and
researchers can develop more sophisticated algorithms or models.


%prep
%setup -q -n maple%{version}

%build
echo "Nothing to do"  # Nothing to do

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/
mkdir -p $RPM_BUILD_ROOT/etc/init.d

#The link below is a temp fix only and should be corrected by maple at some point
cd bin.SUN_SPARC_SOLARIS/sparcv8plusa
ln -s libgmp.so.3.4.1 libgmp.so.3.3.3
cd ../../../

# Copy the stuff to the build root
/usr/local/gnu/bin/cp -r maple12 $RPM_BUILD_ROOT/usr/local/
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/local/maple12/README.rutgers
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/init.d/maple

cd $RPM_BUILD_ROOT/usr/local
ln -s maple12 maple


%post
cat <<EOF
 
====================================================================
 You might want to make a /etc/rc2.d/maple link, to start the maple
 license server at boot time
 ln -s /etc/init.d/maple /etc/rc2.d/S99maple

 Read the README.rutgers for more hints on setting this software up
 for use at Rutgers.  This file is located in /usr/local/maple12.
====================================================================

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /usr/local/maple12
/usr/local/maple12/*
/usr/local/maple
%attr(755,root,root)/etc/init.d/maple

%changelog
* Thu Jul 31 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 12-2
- changes to maple12.README.rutgers
* Thu Jun 26 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 12-1
- bumped to 12
- changed install path to /usr/local/maple12 and not /usr/local/maple12/maple12
- updated path and version number references in init.d script and README
- updated license file name in init.d script

* Thu Feb 14 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 11-4
- used gnu cp instead of sun cp so that symbolic links are preserved

* Wed Feb 13 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 11-2
- added temp link fix and switched to AutoReq and AutoProv
