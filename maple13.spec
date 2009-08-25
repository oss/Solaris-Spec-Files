Name: 		maple
Version:	13
Release: 	1
Group:		Applications/Mathematics
License:	Commercial
URL:		http://www.maplesoft.com
Source0:	maple%{version}.tar.gz
Source1: 	maple%{version}.README.rutgers
Source2: 	maple%{version}.init.d
BuildRoot:	/var/tmp/%{name}-%{version}-%{release}-root

# Disable find_requires and find_provides
AutoReq:	0
AutoProv:	0

Summary:	Mathematics and simulation software

%description
Maple is a powerful tool for researchers, teachers, and students in 
any technical discipline. It can be used to explore, visualize, and 
solve even the most complex mathematical problems.

%prep
%setup -q -n maple%{version}

%build
echo "Nothing to build."

%install
mkdir -p %{buildroot}%{_prefix}

#The link below is a temp fix only and should be corrected by maple at some point
cd bin.SUN_SPARC_SOLARIS/sparcv8plusa
ln -s libgmp.so.3.4.1 libgmp.so.3.3.3

# Copy the stuff to the build root
%{__cp} -r $RPM_BUILD_DIR/maple%{version} %{buildroot}%{_prefix}/
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/maple%{version}/README.rutgers
%{__install} -D -m 0755 %{SOURCE2} %{buildroot}/etc/init.d/maple

cd %{buildroot}%{_prefix}
ln -s maple%{version} maple

%post
cat << EOF
 
====================================================================
 You might want to make a /etc/rc2.d/maple link, to start the maple
 license server at boot time:
 ln -s /etc/init.d/maple /etc/rc2.d/S99maple

 Read the README.rutgers for more hints on setting this software up
 for use at Rutgers. This file is located in /usr/local/maple%{version}.
====================================================================

EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_prefix}/maple%{version}/
%{_prefix}/maple
/etc/init.d/maple

%changelog
* Mon Aug 24 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 13-1
- Updated to maple 13

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
