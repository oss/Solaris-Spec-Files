%define name vacation
%define version 0.1
%define release 1
%define prefix /usr/bin

Summary: reply to mail automatically
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Source0: http://www.ayradyss.org/programs/distrib/vacation.tar.gz
BuildRoot: /tmp/free/%{name}-root

%description
vacation automatically replies to incoming mail.

%prep
%setup -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}

install -c -m 555 $RPM_BUILD_DIR/%{name}/vacation.orig $RPM_BUILD_ROOT%{prefix}/vacation

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, bin, bin)
%{prefix}/vacation
