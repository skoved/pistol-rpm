Name:           ffmpegthumbnailer
Version:        2.2.3
Release:        %autorelease
Summary:        Lightweight video thumbnailer that can be used by file managers to create thumbnails for video files 

%global common_description %{expand:
FFmpegthumbnailer is a lightweight video thumbnailer that can be used by file
managers to create thumbnails for your video files. The thumbnailer uses ffmpeg
to decode frames from the video files, so supported videoformats depend on the
configuration flags of ffmpeg.}

License:        GPL-2.0-only
URL:            https://github.com/dirkvdb/ffmpegthumbnailer
Source0:        https://github.com/dirkvdb/ffmpegthumbnailer/archive/refs/tags/%{version}.tar.gz

BuildRequires: gcc
BuildRequires: g++
BuildRequires: cmake
BuildRequires: ffmpeg-free-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-turbo-devel

Requires: /usr/bin/ffmpeg
Requires: libpng
Requires: libjpeg-turbo

%description %{common_description}

%prep
%autosetup

%build
export CMAKE_C_COMPILER=gcc
export CMAKE_CXX_COMPILER=g++
%cmake
%cmake_build


%install
%cmake_install

%check
%ctest

%files
%license COPYING
%doc README.md README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_includedir}/lib%{name}/*
%{_libdir}/lib%{name}/*
/usr/lib/debug/usr/*


%changelog
%autochangelog
