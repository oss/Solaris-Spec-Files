%define name webtools_mailman
%define version 0.1
%define release 2
%define prefix /usr/local

Summary: Web application allowing users to configure Mailman
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Source0: %{name}-%{version}.tar 
BuildRoot: %{_tmppath}/%{name}-root
Requires: webtools >= 0.4 pear-DB pear-HTML pear-Mail pear-Log

%description
This is an addon package to webtools. These tools are an addon to assist
Mailman's lack of user tools to do things such as request a new password,
list the members of a particular list, look at the configuration of a 
particular list, etc.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}
mkdir -p -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}/webbin

cp -R html $RPM_BUILD_ROOT%{prefix}/%{name}/

%post
cat << EOF
The README is located in /usr/local/doc/webtools_whitelist/.

Be sure to run the following:
ln -s /var/lib/mailman/bin/remove_members \
    %{prefix}/%{name}/webbin/remove_members
ln -s /usr/lib/mailman/bin/newlist \
    %{prefix}/%{name}/webbin/newlist
ln -s /usr/lib/mailman/bin/list_members \
    %{prefix}/%{name}/webbin/list_members
ln -s /var/lib/mailman/bin/list_lists \
    %{prefix}/%{name}/webbin/list_lists
ln -s /usr/lib/mailman/bin/find_member \
    %{prefix}/%{name}/webbin/find_member
ln -s /var/lib/mailman/bin/dumpdb \
    %{prefix}/%{name}/webbin/dumpdb
ln -s /usr/lib/mailman/bin/config_list \
    %{prefix}/%{name}/webbin/config_list
ln -s /usr/lib/mailman/bin/change_pw \
    %{prefix}/%{name}/webbin/change_pw

Be advised that the programs linked to should be mode 555.

EOF

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, www, www)
%doc README
%{prefix}/%{name}/html/*
%dir %{prefix}/%{name}/webbin

