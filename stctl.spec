Summary: Solaris SCSI Tape Changer Controller
Name: stctl
Version: 1.2.5
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: stctl.tar.gz
BuildRoot: %{_tmppath}/%{name}-root


%description
SCSI Tape Changer http://www.cs.pdx.edu/~eric/stctl/


%prep
%setup -q -n stctl

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/kernel/drv
mkdir -p %{buildroot}/usr/sbin

%ifarch sparc
install -m 0755 stctl %{buildroot}/usr/kernel/drv/stctl
install -m 0755 stc %{buildroot}/usr/sbin/stc
%endif

%ifarch sparc64
install -m 0755 stctl64 %{buildroot}/usr/kernel/drv/stctl64
install -m 0755 stc64 %{buildroot}/usr/sbin/stc64
%endif

install -m 0644 stctl.conf    %{buildroot}/usr/kernel/drv/stctl.conf

%clean
rm -rf %{buildroot}

%post
echo <<EOF
1. You need to configure /usr/kernel/drv/stctl.conf according
   to http://www.cs.pdx.edu/~eric/stctl/stctl-conf.html

2. Add the following line to /etc/devlink.tab :

   type=ddi_pseudo;name=stctl      rmt/stctl\N0 

   NOTE: A <TAB> MUST separate these two items 

3. add_drv -m '* 0660 root sys' stctl

You must do these steps in order, step 3 will fail if
the stctl.conf is misconfigured.
EOF

%files
%defattr(-, root, root)
/usr/kernel/drv/stctl*
/usr/sbin/stc*
