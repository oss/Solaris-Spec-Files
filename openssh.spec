%include perl-header.spec

Name: openssh
Version: 3.1p1
Release: 1ru
Summary: Secure Shell - telnet alternative (and much more)
Group: Cryptography
License: BSD
Source: %{name}-%{version}.tar.gz
Patch: %{name}-3.0.2p1.patch
BuildRoot: /var/tmp/%{name}-%{version}-root
BuildRequires: perl > 5.0.0
BuildRequires: openssl zlib-devel prngd patch make
# %if %{max_bits} == 64
# BuildRequires: vpkg-SUNWzlibx
# %endif
Requires: openssl
Requires: zlib
Requires: prngd

%description
OpenSSH is based on the last free version of Tatu Ylonen's sample
implementation with all patent-encumbered algorithms removed (to 
external libraries), all known security bugs fixed, new features 
reintroduced and many other clean-ups.  OpenSSH has been created by
Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt,
and Dug Song. It has a homepage at http://www.openssh.com/  (from README)

This version of openssh is patched to enable a non-setuid client.

%prep
%setup -q
PATH="/usr/local/gnu/bin:$PATH"
export PATH
%patch -p1

%build
#%if %{max_bits} == 64
# no 64-bit Rutgers PAM, so we build 32 bits only.
# CC="/opt/SUNWspro/bin/cc -xarch=v9" \
#   ./configure --prefix=/usr/local --with-ssl-dir=/usr/local/ssl/sparcv9 \
#   --with-pam --with-prngd-socket=/var/run/urandom
#./configure --prefix=/usr/local --with-ssl-dir=/usr/local/ssl --with-pam \
#  --with-prngd-socket=/var/run/urandom --disable-suid-ssh
#%else
./configure --prefix=/usr/local --with-ssl-dir=/usr/local/ssl --with-pam \
  --with-prngd-socket=/var/run/urandom --disable-suid-ssh
#%endif
/usr/local/gnu/bin/gmake

%install
rm -fr %{buildroot}
# We need to use Sun strip:
PATH="/usr/ccs/bin:/usr/local/gnu/bin:$PATH"
export PATH
gmake install DESTDIR=%{buildroot}
cp ssh_prng_cmds %{buildroot}/usr/local/etc/


# move config files to xxx.rpm so as not to stomp on existing config files
cd %{buildroot}/usr/local/etc
mv ssh_config ssh_config.rpm
mv ssh_prng_cmds ssh_prng_cmds.rpm
mv sshd_config sshd_config.rpm

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,bin)
/usr/local/

%post
cat <<EOF
Notes:

1) Keys are required for this machine to act as a host.
   To generate new keys, do this:

cd /usr/local/bin
./ssh-keygen -t rsa1 -f /usr/local/etc/ssh_host_key -N ""
./ssh-keygen -t rsa -f /usr/local/etc/ssh_host_rsa_key -N ""
./ssh-keygen -t dsa -f /usr/local/etc/ssh_host_dsa_key -N ""

2) The default config files in /usr/local/etc are not "active."
   To activate them, remove the .rpm suffix.

3) ssh requires prngd to be running with a socket in /var/run.  Run

prngd /var/run/urandom

  as root.

EOF

%changelog
* Thu Dec 13 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to OpenSSH 3.0.2p1
