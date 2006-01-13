%define name 	 postfixadmin
%define version 2.1.0
%define release  1 
%define prefix   /usr/local

Summary:	Web
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Postfix Admin User License Agreement
Group:		Networking/Other
Source0:	%{name}-%{version}.tgz
URL:		http://high5.net/postfixadmin/
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: apache >= 1.3.27 php >= 4.1

%description
Postfix Admin is a Web Based Management tool created for Postfix.
It is a PHP based application that handles Postfix Style Virtual 
Domains and Users that are stored in MySQL.

Postfix Admin supports:
- Virtual Mailboxes / Virtual Aliases / Forwarders.
- Domain to Domain forwarding / Catch-All.
- Vacation (auto-response) for Virtual Mailboxes.
- Quota / Alias & Mailbox limits per domain.
- Backup MX.

Requirements:
- Postfix 2.0 or higher.
- Apache 1.3.27 or higher.
- PHP 4.1 or higher.
- MySQL 3.23.xx or higher.

%prep
%setup -q -n postfixadmin-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}
cd ..
cp -R postfixadmin-%{version} $RPM_BUILD_ROOT%{prefix}
cd $RPM_BUILD_ROOT%{prefix}
mv postfixadmin-%{version} postfixadmin
cd $RPM_BUILD_ROOT%{prefix}/postfixadmin/
chmod 644 *\.php *\.css
cd $RPM_BUILD_ROOT%{prefix}/postfixadmin/admin/
chmod 644 *.php .ht*
cd $RPM_BUILD_ROOT%{prefix}/postfixadmin/images/
chmod 644  *\.png
cd $RPM_BUILD_ROOT%{prefix}/postfixadmin/languages/
chmod 644 *.lang
cd $RPM_BUILD_ROOT%{prefix}/postfixadmin/templates/
chmod 644 *.tpl
cd $RPM_BUILD_ROOT%{prefix}/postfixadmin/users/
chmod 644 *\.php

%post
echo "postfixadmin has been installed"

%clean
[ %{buildroot} != "/" ] && [ -d %{buildroot} ] && rm -rf %{buildroot};

%files
%defattr(-,root,root)
%{prefix}/postfixadmin/
