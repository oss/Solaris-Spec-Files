Summary: inews news posting program (from inn distribution)
Name: inews
Version: 2.3.2
Release: 2
Copyright: BSD
Group: Applications/Internet
Source: inn-%{version}.tar.gz
BuildRequires: perl
BuildRoot: /var/tmp/%{name}-root

%description
Inews reads a Usenet news  article  (perhaps  with  headers) from  the
named file or standard input if no file is given.  It adds some headers
and performs some  consistency  checks.  If  the article does not meet
these checks (for example, too much quoting of old articles,  or
posting  to  non-existent newsgroups)  then the article is rejected.
If it passes the checks, inews sends the article to the local news
server  as specified in the inn.conf(5) file for distribution.

  [ from inews(1) ]

%prep
%setup -q -n inn-%{version}

%build
LD="/usr/ccs/bin/ld" LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CCFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  ./configure --with-sendmail=/usr/lib/sendmail
make

%install
rm -rf $RPM_BUILD_ROOT
for i in lib/news man/man1 inn/etc ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done
mkdir $RPM_BUILD_ROOT/usr/lib

mv frontends/inews $RPM_BUILD_ROOT/usr/local/lib/news
mv doc/man/inews.1 $RPM_BUILD_ROOT/usr/local/man/man1
cat <<EOF > $RPM_BUILD_ROOT/usr/local/inn/etc/inn.conf.rpm
##  $Revision$
##  inn.conf -- inn configuration data
##  Format:
##      <parameter>:<whitespace><value>
##  Used by various programs and libinn.  The following parameters are defined:
##      domain          Local domain, without leading period.
##      fromhost        What to put in the From line; default is FQDN
##                      of the local host.
##      moderatormailer Where to mail moderated postings, if not found
##                      in the moderators file; see moderators(5).
##      pathhost        What to put in the Path and Xref headers; default
##                      is FQDN of the local host.
##      organization    If $ORGANIZATION doesn't exist.  What to put in
##                      the Organization header if blank.
##      server          If $NNTPSERVER doesn't exist.  Local NNTP server
##                      host to connect to.
##
organization:           Rutgers University
server:                 news-nb.rutgers.edu
moderatormailer:        rutgers.edu
EOF

cd $RPM_BUILD_ROOT/usr/lib
ln -s ../local/lib/news news

%post
echo "Move /usr/local/inn/etc/inn.conf.rpm to complete the installation"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/news/inews
/usr/local/man/man1/inews.1
%attr(644,news,other) /usr/local/inn/etc/inn.conf.rpm
/usr/lib/news
