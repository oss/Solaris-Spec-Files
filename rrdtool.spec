%include perl-header.spec

Summary: 		RRDtool - round robin database
Name: 			rrdtool
Version: 		1.0.38
Release:		1ru
Copyright: 		GPL
Group: 			Applications/Databases
Source: 		http://www.caida.org/Tools/RRDtool/pub/%{name}-%{version}.tar.gz
#Patch:			rrdtool-rrdtutorial.pod.patch
Buildroot: 		/var/tmp/rrdtool-root
Prefix:	 		%{_prefix}
#BuildRequires:	tcl
Url: 			http://www.caida.org/Tools/RRDtool/
Vendor: 		Tobi Oetiker <oetiker@ee.ethz.ch>

%description
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature, 
server load average). It stores the data in a very compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

%prep
%setup -q

%build
PATH="%{perl_prefix}/bin:$PATH"
export PATH

LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  DFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CFLAGS="-I/usr/local/include" LD_RUN_PATH="/usr/local/lib" \
  CC="gcc" ./configure --prefix=/usr/local/rrdtool --disable-nls

echo > doc/rrdtutorial.es.pod

make

%install
PATH="%{perl_prefix}/bin:$PATH"
export PATH

rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{site_perl_arch}
mv $RPM_BUILD_ROOT/usr/local/rrdtool/lib/perl/* $RPM_BUILD_ROOT/%{site_perl_arch}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/usr/local/rrdtool/lib/librrd.la
/usr/local/rrdtool/lib/librrd.a
%{site_perl_arch}/
/usr/local/rrdtool/bin/rrdcgi
/usr/local/rrdtool/bin/rrdtool
/usr/local/rrdtool/bin/rrdupdate
/usr/local/rrdtool/bin/trytime
/usr/local/rrdtool/include/rrd.h
/usr/local/rrdtool/doc/rrdtool.pod
/usr/local/rrdtool/doc/rrdlast.pod
/usr/local/rrdtool/doc/rrdcreate.pod
/usr/local/rrdtool/doc/rrdupdate.pod
#/usr/local/rrdtool/doc/rrdtutorial.es.pod
/usr/local/rrdtool/doc/cdeftutorial.pod
/usr/local/rrdtool/doc/rpntutorial.pod
/usr/local/rrdtool/doc/rrdgraph.pod
/usr/local/rrdtool/doc/bin_dec_hex.pod
/usr/local/rrdtool/doc/rrdfetch.pod
/usr/local/rrdtool/doc/rrdrestore.pod
/usr/local/rrdtool/doc/rrddump.pod
/usr/local/rrdtool/doc/rrdtune.pod
/usr/local/rrdtool/doc/rrdresize.pod
/usr/local/rrdtool/doc/rrdcgi.pod
/usr/local/rrdtool/doc/rrdtutorial.pod
/usr/local/rrdtool/doc/rrdinfo.pod
/usr/local/rrdtool/doc/rrdxport.pod
/usr/local/rrdtool/doc/rrdtool.txt
/usr/local/rrdtool/doc/rrdlast.txt
/usr/local/rrdtool/doc/rrdcreate.txt
/usr/local/rrdtool/doc/rrdupdate.txt
#/usr/local/rrdtool/doc/rrdtutorial.es.txt
/usr/local/rrdtool/doc/cdeftutorial.txt
/usr/local/rrdtool/doc/rpntutorial.txt
/usr/local/rrdtool/doc/rrdgraph.txt
/usr/local/rrdtool/doc/bin_dec_hex.txt
/usr/local/rrdtool/doc/rrdfetch.txt
/usr/local/rrdtool/doc/rrdrestore.txt
/usr/local/rrdtool/doc/rrddump.txt
/usr/local/rrdtool/doc/rrdtune.txt
/usr/local/rrdtool/doc/rrdresize.txt
/usr/local/rrdtool/doc/rrdcgi.txt
#/usr/local/doc/rrdtutorial.txt
/usr/local/rrdtool/doc/rrdinfo.txt
/usr/local/rrdtool/doc/rrdxport.txt
/usr/local/rrdtool/doc/RRDs.txt
/usr/local/rrdtool/doc/RRDp.txt
/usr/local/rrdtool/html/rrdtool.html
/usr/local/rrdtool/html/rrdlast.html
/usr/local/rrdtool/html/rrdcreate.html
/usr/local/rrdtool/html/rrdupdate.html
#/usr/local/rrdtool/html/rrdtutorial.es.html
/usr/local/rrdtool/html/cdeftutorial.html
/usr/local/rrdtool/html/rpntutorial.html
/usr/local/rrdtool/html/rrdgraph.html
/usr/local/rrdtool/html/bin_dec_hex.html
/usr/local/rrdtool/html/rrdfetch.html
/usr/local/rrdtool/html/rrdrestore.html
/usr/local/rrdtool/html/rrddump.html
/usr/local/rrdtool/html/rrdtune.html
/usr/local/rrdtool/html/rrdresize.html
/usr/local/rrdtool/html/rrdcgi.html
/usr/local/rrdtool/html/rrdtutorial.html
/usr/local/rrdtool/html/rrdinfo.html
/usr/local/rrdtool/html/rrdxport.html
/usr/local/rrdtool/html/RRDs.html
/usr/local/rrdtool/html/RRDp.html
/usr/local/rrdtool/man/man1/rrdtool.1
/usr/local/rrdtool/man/man1/rrdlast.1
/usr/local/rrdtool/man/man1/rrdcreate.1
/usr/local/rrdtool/man/man1/rrdupdate.1
#/usr/local/rrdtool/man/man1/rrdtutorial.es.1
/usr/local/rrdtool/man/man1/cdeftutorial.1
/usr/local/rrdtool/man/man1/rpntutorial.1
/usr/local/rrdtool/man/man1/rrdgraph.1
/usr/local/rrdtool/man/man1/bin_dec_hex.1
/usr/local/rrdtool/man/man1/rrdfetch.1
/usr/local/rrdtool/man/man1/rrdrestore.1
/usr/local/rrdtool/man/man1/rrddump.1
/usr/local/rrdtool/man/man1/rrdtune.1
/usr/local/rrdtool/man/man1/rrdresize.1
/usr/local/rrdtool/man/man1/rrdcgi.1
/usr/local/rrdtool/man/man1/rrdtutorial.1
/usr/local/rrdtool/man/man1/rrdinfo.1
/usr/local/rrdtool/man/man1/rrdxport.1
/usr/local/rrdtool/man/man1/RRDs.1
/usr/local/rrdtool/man/man1/RRDp.1
/usr/local/rrdtool/examples/cgi-demo.cgi
/usr/local/rrdtool/examples/piped-demo.pl
/usr/local/rrdtool/examples/shared-demo.pl
/usr/local/rrdtool/examples/stripes.pl
/usr/local/rrdtool/examples/bigtops.pl
/usr/local/rrdtool/examples/minmax.pl
/usr/local/rrdtool/contrib/trytime/README
/usr/local/rrdtool/contrib/trytime/trytime.c
