Summary: Probshell tool
Name: setprobshell
Version: 2
Release: 2
Copyright: Rutgers
Source: setprobshell.tar.gz
Group: System Environment/Shells
BuildRoot: /var/tmp/%{name}-root
Requires: probshell

%description
Setprobshell is used in conjunction with the probshell package.

%prep
%setup -n setprobshell -T -c
%setup -n setprobshell -D -q -T -a 0

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . | cpio -pdum $RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f | sed "s#$RPM_BUILD_ROOT##" > FILE_LIST

%clean
rm -rf $RPM_BUILD_ROOT

%files -f FILE_LIST
%defattr(-,root,sys)
