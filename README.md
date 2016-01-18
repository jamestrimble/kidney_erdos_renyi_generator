# kidney_erdos_renyi_generator
An Erdos-Renyi generator of random kidney exchange instances

## Usage

For an instance with 100 patients, 10 NDDs, and edge probability 0.6:

```
python kerg/kerg.py 100 10 0.6
```

The instances generated do not contain self-loops from a donor-patient pair to itself.
