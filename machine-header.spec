# Any RPM with machine-dependent filenames should include this header.

%ifos solaris2.8
%define sol_os      solaris2.8
%ifarch sparc64
%define max_bits    64
%else
%define max_bits    32
%endif
%endif

%ifos solaris2.7
%define sol_os      solaris2.7
%ifarch sparc64
%define max_bits    64
%else
%define max_bits    32
%endif
%endif

%ifos solaris2.6
%define sol_os      solaris2.6
%define max_bits    32
%endif

%define sparc_arch  sparc-sun-%{sol_os}
%ifarch sparc64
%define real_arch   sparc64-sun-%{sol_os}
%else
%define real_arch   sparc-sun-%{sol_os}
%endif

# Set these to SOLARIS if you want to use the ones bundled with
# Solaris or otherwise provided by Sun:

%define which_gnome REPOSITORY
%define which_perl  REPOSITORY

# Don't forget to use the correct profile with build-r.pl!

