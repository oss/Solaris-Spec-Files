Summary: X11 passphrase grabber
Name: x11-ssh-askpass
Version: 1.2.2
Release: 1
Group: User Interface/X11
License: BSD
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: openssh
BuildRequires: vpkg-SPROcc

%description
X11-SSH-ASKPASS lets you enter passphrases into SSH and SSH-ADD from
an X window, so you don't need to run SSH from a terminal.

%prep
%setup -q

%build
./configure
xmkmf
make includes
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/libexec \
    %{buildroot}/usr/openwin/lib/X11/app-defaults \
    %{buildroot}/usr/local/man/man1
install -m 0755 x11-ssh-askpass %{buildroot}/usr/local/libexec/ssh-askpass
install -m 0444 SshAskpass.ad \
    %{buildroot}/usr/openwin/lib/X11/app-defaults/SshAskPass
install -m 0444 x11-ssh-askpass.man \
    %{buildroot}/usr/local/man/man1/ssh-askpass.1

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc ChangeLog README TODO
/usr/local/man/man1/ssh-askpass.1
/usr/local/libexec/ssh-askpass
/usr/openwin/lib/X11/app-defaults/SshAskPass
