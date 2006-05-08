Summary: System uptime monitoring utility
Name: sysmon
Version: 1.02
Release: 2
Group: System Environment/Base
License: Rutgers
Source0: %{name}-source-1.0-NEW.tar.gz
Source1: %{name}-%{version}-files.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
System uptime monitoring utility.

%prep
%setup -q -n sysmon
%setup -T -D -a 1 -n sysmon

%build
rm -f rst
gcc -o rst rst.c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/etc %{buildroot}/usr/local/bin \
         %{buildroot}/etc/init.d

install -m 0700 rmu.sh    %{buildroot}/usr/local/etc/rmu
install -m 0700 sysmon.sh %{buildroot}/usr/local/etc/sysmon
install -m 0700 cml.sh    %{buildroot}/usr/local/etc/cml
install -m 0700 cdl.sh    %{buildroot}/usr/local/etc/cdl
echo "sysadmin@eden.rutgers.edu" > %{buildroot}/usr/local/etc/rmu_mail.rpm
chmod 0600 %{buildroot}/usr/local/etc/rmu_mail.rpm
install -m 0700 rst       %{buildroot}/usr/local/bin/rst
install -m 0700 files/etc/init.d/sysmon.SAMPLE \
    %{buildroot}/etc/init.d/sysmon.SAMPLE

%clean
rm -rf %{buildroot}

%post
cat <<EOF
If you want this to run upon startup, do the following commands:

        mv /etc/init.d/sysmon.SAMPLE /etc/init.d/sysmon
        chmod 744 /etc/init.d/sysmon
        chown root:sys /etc/init.d/sysmon
        ln -s /etc/init.d/sysmon /etc/rc2.d/SL40sysmon

Edit and move /usr/local/etc/rmu_mail.rpm.
EOF

%files
%attr(-, root, root) /usr/local/etc/*
%attr(-, root, daemon) /usr/local/bin/*
