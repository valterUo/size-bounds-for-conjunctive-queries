\ Model Linear_Programming_Example
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  h(xyzu)
Subject To
 Rel_xy: h(xy) <= 1
 Rel_yz: h(yz) <= 1
 Rel_zu: h(zu) <= 1
 fd_xz->u: - h(xz) + h(xzu) = 0
 fd_yu->x: - h(yu) + h(xyu) = 0
 fd_xzy->uy: - h(xyz) + h(xyzu) = 0
 fd_yuz->xz: - h(yzu) + h(xyzu) = 0
 Monotonicity_x: - h(yzu) + h(xyzu) >= 0
 Monotonicity_y: - h(xzu) + h(xyzu) >= 0
 Monotonicity_z: - h(xyu) + h(xyzu) >= 0
 Monotonicity_u: - h(xyz) + h(xyzu) >= 0
 Submodularity_xy['z']: - h(z) + h(xz) + h(yz) - h(xyz) >= 0
 Submodularity_xy['u']: - h(u) + h(xu) + h(yu) - h(xyu) >= 0
 Submodularity_xy['z',_'u']: - h(zu) + h(xzu) + h(yzu) - h(xyzu) >= 0
 Submodularity_xz['y']: - h(y) + h(xy) + h(yz) - h(xyz) >= 0
 Submodularity_xz['u']: - h(u) + h(xu) + h(zu) - h(xzu) >= 0
 Submodularity_xz['y',_'u']: - h(yu) + h(xyu) + h(yzu) - h(xyzu) >= 0
 Submodularity_xu['y']: - h(y) + h(xy) + h(yu) - h(xyu) >= 0
 Submodularity_xu['z']: - h(z) + h(xz) + h(zu) - h(xzu) >= 0
 Submodularity_xu['y',_'z']: - h(yz) + h(xyz) + h(yzu) - h(xyzu) >= 0
 Submodularity_yz['x']: - h(x) + h(xy) + h(xz) - h(xyz) >= 0
 Submodularity_yz['u']: - h(u) + h(yu) + h(zu) - h(yzu) >= 0
 Submodularity_yz['x',_'u']: - h(xu) + h(xyu) + h(xzu) - h(xyzu) >= 0
 Submodularity_yu['x']: - h(x) + h(xy) + h(xu) - h(xyu) >= 0
 Submodularity_yu['z']: - h(z) + h(yz) + h(zu) - h(yzu) >= 0
 Submodularity_yu['x',_'z']: - h(xz) + h(xyz) + h(xzu) - h(xyzu) >= 0
 Submodularity_zu['x']: - h(x) + h(xz) + h(xu) - h(xzu) >= 0
 Submodularity_zu['y']: - h(y) + h(yz) + h(yu) - h(yzu) >= 0
 Submodularity_zu['x',_'y']: - h(xy) + h(xyz) + h(xyu) - h(xyzu) >= 0
 Subadditivity_('x',)('x',): h(x) >= 0
 Subadditivity_('x',)('y',): h(x) + h(y) - h(xy) >= 0
 Subadditivity_('x',)('z',): h(x) + h(z) - h(xz) >= 0
 Subadditivity_('x',)('u',): h(x) + h(u) - h(xu) >= 0
 Subadditivity_('y',)('y',): h(y) >= 0
 Subadditivity_('y',)('z',): h(y) + h(z) - h(yz) >= 0
 Subadditivity_('y',)('u',): h(y) + h(u) - h(yu) >= 0
 Subadditivity_('z',)('z',): h(z) >= 0
 Subadditivity_('z',)('u',): h(z) + h(u) - h(zu) >= 0
 Subadditivity_('u',)('u',): h(u) >= 0
 Subadditivity_('x',)('y',_'z'): h(x) + h(yz) - h(xyz) >= 0
 Subadditivity_('x',)('y',_'u'): h(x) + h(yu) - h(xyu) >= 0
 Subadditivity_('x',)('z',_'u'): h(x) + h(zu) - h(xzu) >= 0
 Subadditivity_('y',)('z',_'u'): h(y) + h(zu) - h(yzu) >= 0
 Subadditivity_('x',)('y',_'z',_'u'): h(x) + h(yzu) - h(xyzu) >= 0
Bounds
 h(x) <= 1
 h(y) <= 1
 h(z) <= 1
 h(u) <= 1
 h(xy) <= 2
 h(xz) <= 2
 h(xu) <= 2
 h(yz) <= 2
 h(yu) <= 2
 h(zu) <= 2
 h(xyz) <= 3
 h(xyu) <= 3
 h(xzu) <= 3
 h(yzu) <= 3
 h(xyzu) <= 4
End
