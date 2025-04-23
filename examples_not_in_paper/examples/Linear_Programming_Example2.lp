\ Model Linear_Programming_Example
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  h(xyz)
Subject To
 R0: h(xy) <= 1
 R1: h(yz) <= 1
 R2: h(xz) <= 1
 R3: - h(yz) + h(xyz) >= 0
 R4: - h(xz) + h(xyz) >= 0
 R5: - h(xy) + h(xyz) >= 0
 R6: - h(z) + h(xz) + h(yz) - h(xyz) >= 0
 R7: - h(y) + h(xy) + h(yz) - h(xyz) >= 0
 R8: - h(x) + h(xy) + h(xz) - h(xyz) >= 0
Bounds
End
