# -*- coding: utf-8 -*-
#
import numpy

from ._helpers import E2rScheme
from ..helpers import article

_citation = article(
    authors=["Ann Haegemans", "Robert Piessens"],
    title="Construction of Cubature Formulas of Degree Seven and Nine Symmetric Planar Regions Using Orthogonal Polynomials",
    journal="SIAM Journal on Numerical Analysis",
    volume="14",
    number="3",
    month="jun",
    year="1977",
    pages="492-508",
    url="https://www.jstor.org/stable/2156699",
)


def haegemans_piessens_a():
    points = numpy.array(
        [
            [+0.45825756949558400066e1, +0.45825756949558400066e1],
            [+0.45825756949558400066e1, -0.45825756949558400066e1],
            [-0.45825756949558400066e1, +0.45825756949558400066e1],
            [-0.45825756949558400066e1, -0.45825756949558400066e1],
            [+0.70236144020646152963e1, 0.0],
            [-0.70236144020646152963e1, 0.0],
            [+0.16302145109770590301e1, 0.0],
            [-0.16302145109770590301e1, 0.0],
            [0.0, +0.88693729743104806995e1],
            [0.0, -0.88693729743104806995e1],
            [0.0, +0.27097193301071890633e1],
            [0.0, -0.27097193301071890633e1],
        ]
    )
    weights = numpy.array(
        [
            0.53428446489622333987e-1,
            0.53428446489622333987e-1,
            0.53428446489622333987e-1,
            0.53428446489622333987e-1,
            0.32645130906584894203e-1,
            0.32645130906584894203e-1,
            0.20960123475066223175e1,
            0.20960123475066223175e1,
            0.74005652121778807454e-2,
            0.74005652121778807454e-2,
            0.89867771698516347806,
            0.89867771698516347806,
        ]
    )
    return E2rScheme("Haegemans-Piessens 7", weights, points, 7, _citation)


def haegemans_piessens_b():
    points = numpy.array(
        [
            [+0.31445132948861316205e1, +0.17968204012034815825e1],
            [+0.31445132948861316205e1, -0.17968204012034815825e1],
            [-0.31445132948861316205e1, +0.17968204012034815825e1],
            [-0.31445132948861316205e1, -0.17968204012034815825e1],
            [+0.81288621554158904245e1, +0.56975989672929856102e1],
            [+0.81288621554158904245e1, -0.56975989672929856102e1],
            [-0.81288621554158904245e1, +0.56975989672929856102e1],
            [-0.81288621554158904245e1, -0.56975989672929856102e1],
            [+0.31047512376040704732e1, +0.75872948955819104799e1],
            [+0.31047512376040704732e1, -0.75872948955819104799e1],
            [-0.31047512376040704732e1, +0.75872948955819104799e1],
            [-0.31047512376040704732e1, -0.75872948955819104799e1],
            [+0.88003944155658680273e1, 0.0],
            [-0.88003944155658680273e1, 0.0],
            [0.0, +0.34241487633426925811e1],
            [0.0, -0.34241487633426925811e1],
            [0.0, +0.14237038816700630838e2],
            [0.0, -0.14237038816700630838e2],
            [0.0, 0.0],
        ]
    )
    weights = numpy.array(
        [
            0.42891635372364421816,
            0.42891635372364421816,
            0.42891635372364421816,
            0.42891635372364421816,
            0.21828892485177877829e-2,
            0.21828892485177877829e-2,
            0.21828892485177877829e-2,
            0.21828892485177877829e-2,
            0.93469649142381572351e-2,
            0.93469649142381572351e-2,
            0.93469649142381572351e-2,
            0.93469649142381572351e-2,
            0.61187144873852822063e-2,
            0.61187144873852822063e-2,
            0.46279666238296101906,
            0.46279666238296101906,
            0.54938772079738427117e-4,
            0.54938772079738427117e-4,
            0.35834598443491337448e1,
        ]
    )
    return E2rScheme("Haegemans-Piessens 9", weights, points, 9, _citation)
