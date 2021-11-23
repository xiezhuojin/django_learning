## MultiPartParserError(Exception)

## InputStreamExhausted(Exception)


## MultiPartParser
* A rfc2388 multipart/form-data parser. `MultiValueDict.parse()` reads the input stream in `chunk_size` chunks and returns a tuple of `(MultiValueDict(POST), MultiValueDict(FILES))`.

> [\__init__] init the MultiPartParser object, which setups [self._boundary], [self._input_data] (from parameter), [self._chunk_size], [self._meta], [self._encoding], [self._content_length], [self._upload_handlers] (from parameter).

> [parse] parse the POST data and break it into a FILES MultiValueDict and a POST MultiValueDict. return a tuple containing the POST and FILES dictionary, respectively.
<!-- TODO: continue here -->

## LazyStream
* The LazyStream wrapper allows one to get and "unget" bytes from a stream.

## ChunkIter
* an iterable that will yield chunks of data. Given a file-like object as the constructor, yield chunks of read operations form that object.

## InterBoundaryIter
* a producer that  will iterate over boundaries.

## BoundaryIter
* will happily yield bytes until a boundary is found. Will yield the bytes before the boundary, throw away the boundary bytes themselves, and push the post-boundary bytes back on the stream.

## exhaust
* exhaust an iterator or stream.

## parse_boundary_stream
* parse one stream that encapsulates a boundary.

## Parser
> [\__init__] setup [self._stream] and [self._separator].

> [\__inter__] return a stream separated by boundary

## parse_header
* parse the header into a key-value, for example: "multipart/form-data; boundary=something" into {"multipart/form-data": {"boundary": "something"}}.

## _parse_header_params
* parse string like ";a;b;c" into ["a", "b", "c"].
