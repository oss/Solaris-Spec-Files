Name: nn
Version: 6.5.6
Summary: NN newsreader
Release: 2
Copyright: BSD-like
Source: nn.tar.Z
Patch: nn.patch
Group: Applications/Internet
BuildRoot: /var/tmp/%{name}-root

%description
NN is a popular and powerful newsreader.  Install this if you want to
read Usenet news.

%prep
%setup -q
%patch
cp config.h-dist config.h

%build
make ymakefile
perl -i -p -e 's/TERMLIB/\$(TERMLIB)/' ymakefile
make TERMLIB="-ltermlib -lsocket -lnsl"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir $RPM_BUILD_ROOT/usr/local/man/man8
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/nn/help

cp nnusage $RPM_BUILD_ROOT/usr/local/bin/nnusage
cp nngrab $RPM_BUILD_ROOT/usr/local/bin/nngrab
cp nnstats $RPM_BUILD_ROOT/usr/local/bin/nnstats
for i in nn nnview nnbatch nnpost nngrep nngoback nntidy nnadmin nncheck ; do
    cp nn $RPM_BUILD_ROOT/usr/local/bin/$i
done

for i in nn nncheck nngoback nngrab nngrep nnpost nntidy nnview ; do
    cp man/$i.1 $RPM_BUILD_ROOT/usr/local/man/man1/$i.1
done

for i in nnstats nnadmin nnusage ; do
    cp man/$i.1m $RPM_BUILD_ROOT/usr/local/man/man1/$i.1m
done

cp man/nnmaster.8 $RPM_BUILD_ROOT/usr/local/man/man8/nnmaster.8
cp man/nnspew.8 $RPM_BUILD_ROOT/usr/local/man/man8/nnspew.8

for i in help/* ; do
    cp $i $RPM_BUILD_ROOT/usr/local/lib/nn/$i
done

for i in upgrade_rc aux ; do
    cp $i $RPM_BUILD_ROOT/usr/local/lib/nn/$i
done

tar cf - conf | (cd $RPM_BUILD_ROOT/usr/local/lib && tar xvf -)

echo "news-nb.rutgers.edu" > $RPM_BUILD_ROOT/usr/local/lib/nn/nntp_server

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc olddocs/README
/usr/local/lib/nn
/usr/local/bin/nn
/usr/local/bin/nnusage
/usr/local/bin/nngrab
/usr/local/bin/nnstats
/usr/local/bin/nncheck
/usr/local/bin/nngoback
/usr/local/bin/nngrep
/usr/local/bin/nnpost
/usr/local/bin/nntidy
/usr/local/bin/nnview
/usr/local/bin/nnbatch
/usr/local/man/man1/nn.1
/usr/local/man/man1/nnusage.1m
/usr/local/man/man1/nnstats.1m
/usr/local/man/man1/nncheck.1
/usr/local/man/man1/nngoback.1
/usr/local/man/man1/nngrab.1
/usr/local/man/man1/nngrep.1
/usr/local/man/man1/nnpost.1
/usr/local/man/man1/nntidy.1
/usr/local/man/man1/nnview.1
/usr/local/man/man1/nnadmin.1m
/usr/local/man/man8/nnspew.8
/usr/local/man/man8/nnmaster.8
