%define src_nam  ssh-scripts-1.0

Summary: Default ssh packages to install on a generic machine.
Name: task-ssh
Version: 1.0
Release: 2ru
Group: Administration
License: ---
Source: %{src_nam}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

Requires: egd
Requires: prngd
Requires: openssh
Requires: openssl
Requires: perl
Requires: x11-ssh-askpass

%description
This package only contains startup scripts for egd, prngd, and sshd.  It is
used with apt to automatically install all required subpackages.

%prep
%setup -q -n %{src_nam}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/init.d %{buildroot}/etc/rc2.d %{buildroot}/etc/rc0.d
install -m 0755 egd-ctl %{buildroot}/etc/init.d/ru_egd
install -m 0755 sshd-ctl %{buildroot}/etc/init.d/ru_sshd
ln -s ../init.d/ru_egd %{buildroot}/etc/rc2.d/DONT.S80ru_egd
ln -s ../init.d/ru_egd %{buildroot}/etc/rc0.d/DONT.K11ru_egd
ln -s ../init.d/ru_sshd %{buildroot}/etc/rc2.d/DONT.S81ru_sshd
ln -s ../init.d/ru_sshd %{buildroot}/etc/rc0.d/DONT.K10ru_sshd

%clean
rm -rf %{buildroot}

%post
cat <<EOF
To enable ssh, run the following commands as root:

  mv /etc/rc2.d/DONT.S80ru_egd /etc/rc2.d/S80ru_egd
  mv /etc/rc0.d/DONT.K11ru_egd /etc/rc2.d/K11ru_egd
  
To enable sshd, run the following commands as root:

  mv /etc/rc2.d/DONT.S81ru_sshd /etc/rc2.d/S81ru_sshd
  mv /etc/rc0.d/DONT.K10ru_sshd /etc/rc0.d/K10ru_sshd

and set the PidFile variable in /usr/local/etc/sshd_config to 
"/var/run/sshd.pid".
EOF

%preun
if [ -r /etc/rc0.d/K10ru_sshd ]; then
    echo "You may wish to remove /etc/*.d/*ru_sshd."
fi
if [ -r /etc/rc0.d/K11ru_egd ]; then
    echo "You may wish to remove /etc/*.d/*ru_egd."
fi

%files
%defattr(-,root,root)
/etc/*.d/*

