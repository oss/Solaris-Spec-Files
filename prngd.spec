Summary: Pseudo random-number generator
Name: prngd
Version: 0.9.23
Release: 1
Group: Applications/Productivity
Copyright: GPL
Source: %{name}-%{version}.tar.gz
Patch: %{name}-%{version}.patch
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: patch

%description
- This is the PRNGD "Pseudo Random Number Generator Daemon".
  It offers an EGD compatible interface to obtain random data and is
  intended to be used as an entropy source to feed other software,
  especially software based on OpenSSL.
- Like EGD it calls system programs to collect entropy.
- Unlike EGD it does not generate a pool of random bits that can be
  called from other software.
  Rather more it feeds the bits gathered into its internal PRNG from which
  the "random bits" are obtained when requested. This way, PRNGD is
  never drained and can never block (unlike EGD), so it is also suitable
  to seed inetd-started programs.
  It also features a seed-save file, so that it is immediately usable
  after system start.

  (from 00README)

%prep
%setup -q
%patch -p1

%build
make CC=gcc CFLAGS="-O -DSOLARIS26 -D__EXTENSIONS__" SYSLIBS="-lsocket -lnsl"

%install
rm -rf %{buildroot}

umask 022
mkdir -p %{buildroot}/usr/local/bin %{buildroot}/etc
install -m 0755 prngd %{buildroot}/usr/local/bin/prngd
install -m 0644 contrib/Solaris-7/prngd.conf.solaris-7 \
    %{buildroot}/etc/prngd.conf.rpm

%clean
rm -rf %{buildroot}

%post
touch /etc/prngd-seed
echo "Edit and copy /etc/prngd.conf.rpm."

%preun
rm -f /etc/prngd-seed

%files
%defattr(-,root,bin)
/usr/local/bin/prngd
/etc/prngd.conf.rpm
