Summary: Scheme interpreter
Name: scheme48
Version: 0.56
Release: 2
Group: Development/Languages
Copyright: BSD-type
Source: scheme48-%{version}.tgz
BuildRoot: /var/tmp/%{name}-root

%description
A slightly dated manual reads:

  Scheme 48 is an implementation of the Scheme programming language as
  described in the Revised^4 Report on the Algorithmic Language
  Scheme.  It is based on a compiler and interpreter for a virtual
  Scheme machine.  The name derives from our desire to have an
  implementation that is simple and lucid enough that it looks as if
  it were written in just 48 hours.  We don't claim to have reached
  that stage yet; much more simplification is necessary.

  Scheme 48 tries to be faithful to the upcoming Revised^5 Scheme
  Report, providing neither more nor less in the initial user
  environment.  (This is not to say that more isn't available in other
  environments; see below.)  Support for numbers is weak: bignums are
  slow and floating point is almost nonexistent (see description of
  floatnums, below).  DEFINE-SYNTAX, LET-SYNTAX, LETREC-SYNTAX, and
  SYNTAX-RULES are supported, but not the rest of the Revised^4 Scheme
  macro proposal.


%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local
%ifos solaris2.6
# Solaris 6 is missing this typedef:
cd c/unix
ed socket.c <<__EOTEXT__
    g/^.include/
    a
typedef size_t socklen_t;
.
    w
    q
__EOTEXT__
cd ../..
%endif
make

%install
# Since the make install process hardcodes the destination directory into
# some binaries, we have to duplicate it ourselves.

rm -rf $RPM_BUILD_ROOT

umask 022

for i in lib/scheme48 include bin man/man1 ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done
for i in rts env big opt misc link ; do
    mkdir $RPM_BUILD_ROOT/usr/local/lib/scheme48/$i
done

SCRIPT=$RPM_BUILD_ROOT/usr/local/bin/scheme48

echo '#!/bin/sh' > $SCRIPT
echo >> $SCRIPT
echo 'lib=/usr/local/lib/scheme48' >> $SCRIPT
echo 'exec $lib/scheme48vm -o $lib/scheme48vm -i $lib/scheme48.image "$@"' \
     >> $SCRIPT
chmod +x $SCRIPT

install -m 0755 scheme48vm $RPM_BUILD_ROOT/usr/local/lib/scheme48

for stub in env big opt misc link ; do
    for i in scheme/$stub/*.scm ; do
	install -m 0644 $i $RPM_BUILD_ROOT/usr/local/lib/scheme48/$stub
    done
done

for i in scheme/rts/*num.scm scheme/rts/jar-defrecord.scm ; do
    install -m 0644 $i $RPM_BUILD_ROOT/usr/local/lib/scheme48/rts
done

sed 's=LBIN=/usr/local/bin=g' doc/scheme48.man |
    sed 's=LLIB=/usr/local/lib/scheme48=g' |
    sed 's=LS48=scheme48=g' > scheme48.1
install -m 0644 scheme48.1 $RPM_BUILD_ROOT/usr/local/man/man1
rm scheme48.1

install -m 0644 c/scheme48.h $RPM_BUILD_ROOT/usr/local/include

rm -f /tmp/scheme48.image
build/build-usual-image . /usr/local/lib/scheme48 /tmp/scheme48.image \
   ./scheme48vm build/initial.image
install -m 0644 /tmp/scheme48.image $RPM_BUILD_ROOT/usr/local/lib/scheme48
rm -f /tmp/scheme48.image

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc doc/*
/usr/local/lib/scheme48
/usr/local/man/man1/scheme48.1
/usr/local/bin/scheme48
/usr/local/include/scheme48.h
