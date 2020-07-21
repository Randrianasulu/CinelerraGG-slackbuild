%define ver 20200331
%define cin cinelerra
Summary: Multimedia Editing and construction

%if 0%{?hidepth}
%define xbit 10bit
%define xcfg --enable-x265_hidepth --with-exec-name=cinx
%endif

Name: %{cin}%{?xbit}
Version: 5.1
Release: %{ver}
License: GPL
#Group: Applications/Multimedia
Group: Video
URL: https://cinelerra-gg.org/

# Obtained from :
# git clone git://git.cinelerra.org/goodguy/cinelerra.git cinelerra5
Source0: https://cinelerra-gg.org/download/pkgs/src/cin_%{version}.%{ver}-src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%if 0%{?fedora}
%define rhat 1
%define distro fedora
%endif
%if 0%{?centos}
%define rhat 1
%define distro centos
%define centos_cfg --disable-libaom --disable-libwebp
%endif

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cmake
BuildRequires: binutils
BuildRequires: ctags
BuildRequires: flac-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: lib64usb1.0-devel
BuildRequires: lib64asound-devel
BuildRequires: lib64sndfile-devel
BuildRequires: lib64tiff-devel
#BuildRequires: git
#BuildRequires: inkscape
BuildRequires: lib64png-devel
BuildRequires: lib64xft-devel
BuildRequires: lib64xinerama-devel
BuildRequires: lib64xv-devel
BuildRequires: libtheora-devel
BuildRequires: fftw3-devel
BuildRequires: nasm
BuildRequires: libtool
BuildRequires: ncurses-devel
BuildRequires: perl-libxml-perl
BuildRequires: texinfo
BuildRequires: udftools
BuildRequires: gtk2-devel
BuildRequires: lib64va-devel
BuildRequires: lib64vdpau-devel
%{?rhat:BuildRequires: alsa-lib-devel}
%{?rhat:BuildRequires: bzip2-devel}
%{?rhat:BuildRequires: xorg-x11-fonts-cyrillic}
%{?rhat:BuildRequires: xorg-x11-fonts-cyrillic}
%{?rhat:BuildRequires: xorg-x11-fonts-ISO8859-1-100dpi}
%{?rhat:BuildRequires: xorg-x11-fonts-ISO8859-1-75dpi}
%{?rhat:BuildRequires: xorg-x11-fonts-misc}
%{?rhat:BuildRequires: xorg-x11-fonts-Type1}
%{?suse:BuildRequires: alsa-devel}
%{?suse:BuildRequires: libbz2-devel}
%{?suse:BuildRequires: bitstream-vera-fonts}
%{?suse:BuildRequires: xorg-x11-fonts-core}
%{?suse:BuildRequires: xorg-x11-fonts}
%{?suse:BuildRequires: dejavu-fonts}
%{?suse:BuildRequires: libnuma-devel}
#BuildRequires: xz-devel
BuildRequires: yasm
BuildRequires: zlib-devel

%description
Multimedia editing and construction

%prep
%define _buildsubdir %{cin}-%{version}
%setup -q -n %{cin}-%{version}
%build
./autogen.sh
%configure %{?xcfg} %{?centos_cfg}
%{__make}

%install
%make_install

%clean
%{__rm} -rf %{buildroot}

%if 0%{?rhat}
%post
if [ -d /etc/yum.repos.d ]; then
 echo  > /etc/yum.repos.d/cin.repo "[cin]"
 echo >> /etc/yum.repos.d/cin.repo "name=cinelerra-gg"
 echo >> /etc/yum.repos.d/cin.repo "baseurl=https://cinelerra-gg.org/download/pkgs/%{distro}\$releasever/"
 echo >> /etc/yum.repos.d/cin.repo "enabled=1"
 echo >> /etc/yum.repos.d/cin.repo "gpgcheck=0"
fi
%postun
if [ -d /etc/yum.repos.d ]; then
 rm -f /etc/yum.repos.d/cin.repo
fi
%endif

%files
%defattr(-, root, root, -)
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog

