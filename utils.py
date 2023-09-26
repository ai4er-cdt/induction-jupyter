from __future__ import annotations

import os.path
import urllib.request
import urllib.error

from concurrent.futures import ThreadPoolExecutor
from http.client import HTTPResponse

from tqdm.auto import tqdm
from typing import Sequence, Generator


CHUNK_SIZE = 1024


def greetings() -> None:
	print("Welcome to Cambridge :)")


def guarantee_existence(path: str) -> str:
	if not os.path.exists(path):
		os.makedirs(path)
	return os.path.abspath(path)


def _get_response_size(resp: HTTPResponse) -> None | int:
	"""
	Get the size of the file to download.
	"""
	try:
		return int(resp.info()["Content-length"])
	except (ValueError, KeyError, TypeError):
		return None


def _get_chunks(resp: HTTPResponse) -> Generator[bytes, None]:
	"""
	Generator of the chunks to download.
	"""
	while True:
		chunk = resp.read(CHUNK_SIZE)
		if not chunk:
			break
		yield chunk


def _get_response(url: str) -> HTTPResponse:
	try:
		response = urllib.request.urlopen(url)
	except urllib.error.URLError:
		import ssl
		ssl._create_default_https_context = ssl._create_unverified_context
		req = urllib.request.Request(url)
		req.add_header(
			'user-agent',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
		)
		response = urllib.request.urlopen(req)
	return response


def url_download(url: str, path: str, task: int = 1, total: int = 1) -> None:
	"""
	Download an url to a local file

	See Also
	--------
	downloader : Downloads multiple url in parallel.
	"""
	print(f"Downloading: '{url}' to {path}")
	response = _get_response(url)
	chunks = _get_chunks(response)
	pbar = tqdm(
		desc=f"[{task}/{total}] Requesting {os.path.basename(url)}",
		unit="B",
		total=_get_response_size(response),
		unit_scale=True,
		# format to have current/total size with the full unit, e.g. 60kB/6MB
		# https://github.com/tqdm/tqdm/issues/952
		bar_format="{l_bar}{bar}| {n_fmt}{unit}/{total_fmt}{unit}"
		           " [{elapsed}<{remaining}, {rate_fmt}{postfix}]"
	)
	with pbar as t:
		with open(path, "wb") as file:
			for chunk in chunks:
				file.write(chunk)
				t.update(len(chunk))
			# if done_event.is_set():
			# 	return
	print(f"Downloaded in {path}")


def downloader(urls: Sequence[str], target_dir: str = os.path.abspath("./data")):
	"""
	Downloader to download multiple files in parallel.
	"""
	if isinstance(urls, str):
		urls = [urls]

	with ThreadPoolExecutor(max_workers=4) as pool:
		target_dir = os.path.abspath(target_dir)
		for task, url in enumerate(urls, start=1):
			filename = url.split("/")[-1]
			target_path = os.path.join(target_dir, filename)
			pool.submit(url_download, url, target_path, task, total=len(urls))


def main():
	url = [
		"http://esgdata.gfdl.noaa.gov/thredds/fileServer/gfdl_dataroot3/CMIP/NOAA-GFDL/GFDL-AM4/"
		"amip/r1i1p1f1/Amon/tas/gr1/v20180807/tas_Amon_GFDL-AM4_amip_r1i1p1f1_gr1_198001-201412.nc"
	]
	response = _get_response(url[0])
	print(response)

	target_dist = os.path.abspath("./data")
	downloader(url, target_dist)


if __name__ == '__main__':
	main()
