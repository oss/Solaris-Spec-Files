Summary: Script to report system info to Sun
Name: explorer
Version: 3.1.0
Release: 4
Group: System Environment/Base
Copyright: Sun
Source: explorer.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Script to report system info to Sun

%prep
%setup -q -n explorer -T -c
%setup -q -n explorer -T -D -a 0

%install
rm -rf $RPM_BUILD_ROOT
for i in explorer/tools man/manl sbin ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done

chmod 700 $RPM_BUILD_ROOT/usr/local/explorer/tools
for i in tools/* ; do
    install -m 0500 $i $RPM_BUILD_ROOT/usr/local/explorer/tools
done
install -m 0400 explorer.template \
    $RPM_BUILD_ROOT/usr/local/explorer/explorer.template
install -m 0644 explorer.man $RPM_BUILD_ROOT/usr/local/man/manl/explorer.l
install -m 0500 explorer $RPM_BUILD_ROOT/usr/local/explorer/explorer

cd $RPM_BUILD_ROOT/usr/local/sbin
ln -s ../explorer/explorer explorer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/explorer
/usr/local/sbin/*

%defattr(-,bin,bin)
/usr/local/man/manl/*



