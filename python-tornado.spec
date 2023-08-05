# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-tornado
Epoch: 100
Version: 6.2
Release: 1%{?dist}
Summary: Python web framework and asynchronous networking library
License: Apache-2.0
URL: https://github.com/tornadoweb/tornado/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Tornado is a Python web framework and asynchronous networking library,
originally developed at FriendFeed. By using non-blocking network I/O,
Tornado can scale to tens of thousands of open connections, making it
ideal for long polling, WebSockets, and other applications that require
a long-lived connection to each user.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-tornado
Summary: Python web framework and asynchronous networking library
Requires: python3
Provides: python3-tornado = %{epoch}:%{version}-%{release}
Provides: python3dist(tornado) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tornado = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tornado) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tornado = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tornado) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-tornado
Tornado is a Python web framework and asynchronous networking library,
originally developed at FriendFeed. By using non-blocking network I/O,
Tornado can scale to tens of thousands of open connections, making it
ideal for long polling, WebSockets, and other applications that require
a long-lived connection to each user.

%files -n python%{python3_version_nodots}-tornado
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-tornado
Summary: Python web framework and asynchronous networking library
Requires: python3
Provides: python3-tornado = %{epoch}:%{version}-%{release}
Provides: python3dist(tornado) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tornado = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tornado) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tornado = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tornado) = %{epoch}:%{version}-%{release}

%description -n python3-tornado
Tornado is a Python web framework and asynchronous networking library,
originally developed at FriendFeed. By using non-blocking network I/O,
Tornado can scale to tens of thousands of open connections, making it
ideal for long polling, WebSockets, and other applications that require
a long-lived connection to each user.

%files -n python3-tornado
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-tornado
Summary: Python web framework and asynchronous networking library
Requires: python3
Provides: python3-tornado = %{epoch}:%{version}-%{release}
Provides: python3dist(tornado) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tornado = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tornado) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tornado = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tornado) = %{epoch}:%{version}-%{release}

%description -n python3-tornado
Tornado is a Python web framework and asynchronous networking library,
originally developed at FriendFeed. By using non-blocking network I/O,
Tornado can scale to tens of thousands of open connections, making it
ideal for long polling, WebSockets, and other applications that require
a long-lived connection to each user.

%files -n python3-tornado
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
