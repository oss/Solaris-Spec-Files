#Depricated/EOL package
IgnoreOS: Solaris

Summary: Default ssh packages to install on a generic machine.
Name: task-ssh
Version: 2.0
Release: 1ru
Group: Administration
License: ---
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

Requires: prngd
Requires: openssh
Requires: openssl
Requires: x11-ssh-askpass

%description
This package only contains startup scripts for prngd, and sshd.  It is
used with apt to automatically install all required subpackages.

%prep
%setup -q -n task-ssh-scripts

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/init.d %{buildroot}/etc/rc2.d %{buildroot}/etc/rc0.d
install -m 0755 prngd-ctl %{buildroot}/etc/init.d/ru_prngd
install -m 0755 sshd-ctl %{buildroot}/etc/init.d/ru_sshd
ln -s ../init.d/ru_prngd %{buildroot}/etc/rc2.d/DONT.S80ru_prngd
ln -s ../init.d/ru_prngd %{buildroot}/etc/rc0.d/DONT.K11ru_prngd
ln -s ../init.d/ru_sshd %{buildroot}/etc/rc2.d/DONT.S81ru_sshd
ln -s ../init.d/ru_sshd %{buildroot}/etc/rc0.d/DONT.K10ru_sshd

%clean
rm -rf %{buildroot}

%post
cat <<EOF
To enable ssh, run the following commands as root:

  mv /etc/rc2.d/DONT.S80ru_prngd /etc/rc2.d/S80ru_prngd
  mv /etc/rc0.d/DONT.K11ru_prngd /etc/rc0.d/K11ru_prngd
  mv /etc/prngd.conf.rpm /etc/prngd.conf
  
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
if [ -r /etc/rc0.d/K11ru_prngd ]; then
    echo "You may wish to remove /etc/*.d/*ru_prngd."
fi

%files
%defattr(-,root,bin)
/etc/*.d/*

%changelog
* Mon Dec 17 2001 Sam Isaacson <sbi@nbcs.rutgers.edu>
- Removed egd from package and changed *egd names to *prngd.
- Checked task-ssh scripts into cvs on smeagol.

* Wed Dec 12 2001 Sam Isaacson <sbi@nbcs.rutgers.edu>
- Fixed typographical error in %post and added comment on prngd.conf.
