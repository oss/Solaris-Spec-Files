%define ffversion 1.5.0.4

Name: firefox-flashplugin
Version: 7.0r63
License: Proprietary
Group: Applications/Internet
Summary: Macromedia Flash Player for Mozilla Firefox
Release: 2
Source0: install_flash_player_7_solaris_sparc.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: mozilla-firefox = %{ffversion}

%description
Macromedia Flash Playe for Mozilla Firefox (Netscape or Netscape-compatible).

%prep
%setup -q -n install_flash_player_7_solaris

%build
cat << EOF
Nothing to do!
EOF

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/firefox-%{ffversion}/plugins/

cp flashplayer.xpt libflashplayer.so \
$RPM_BUILD_ROOT/usr/local/lib/firefox-%{ffversion}/plugins/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/usr/local/lib/firefox-%{ffversion}/plugins/*

