Name: autogen
Version: 5.8.3
Copyright: GPL
Group: Development/Tools
Summary: GNU autogen
Release: 5
Source: %{name}-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: m4
Conflicts: vpkg-SFWagen

%description
AutoGen is a tool designed to simplify the creation and maintenance of 
programs that contain large amounts of repetitious text. It is 
especially valuable in programs that have several blocks of text that 
must be kept synchronized.

%prep
%setup -q

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
#if [ -x /usr/local/bin/install-info ] ; then
#	/usr/local/bin/install-info --info-dir=/usr/local/info \
#		 /usr/local/info/autoconf.info
#fi
#if [ -x /usr/local/bin/install-info ] ; then
#        /usr/local/bin/install-info --info-dir=/usr/local/info \
#                 /usr/local/info/standards.info
#fi

#%preun
#if [ -x /usr/local/bin/install-info ] ; then
#	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
#		 /usr/local/info/autoconf.info
#fi
#if [ -x /usr/local/bin/install-info ] ; then
#        /usr/local/bin/install-info --delete --info-dir=/usr/local/info \
#                 /usr/local/info/standards.info
#fi 

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/bin/*
/usr/local/man/man1/*
