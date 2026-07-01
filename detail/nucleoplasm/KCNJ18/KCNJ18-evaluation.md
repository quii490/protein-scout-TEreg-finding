---
type: protein-evaluation
gene: "KCNJ18"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KCNJ18 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KCNJ18 |
| 蛋白名称 | Inward rectifier potassium channel 18 |
| 蛋白大小 | 433 aa / 48.9 kDa |
| UniProt ID | B7U540 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Golgi apparatus; Nucleoplasm (Uncertain) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 433 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=19 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=80.6; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Ig_E-set; IRK_C; K_chnl_inward-rec_Kir |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=15 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- Cytosol; Golgi apparatus; Nucleoplasm (Uncertain)
- PubMed strict=19 broad=32
- AF pLDDT=80.6 PDB=0
- InterPro: Ig_E-set; IRK_C; K_chnl_inward-rec_Kir
- Pfam: IRK; IRK_C; IRK_N
- PPI degree=15 ChIP: None
39333966: Familial hypokalemic periodic paralysis: a case induced by concurrent hyperthyro | 40434516: Molecular genetic analysis of pulmonary benign metastasizing leiomyoma and intra | 35435273: Identification of potential pathogenic genes for severe aplastic anemia by whole

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**Kir2.6内向整流钾通道的核质角色与周期性瘫痪基因**：KCNJ18（Inward rectifier potassium channel 18/Kir2.6, 433 aa, UniProt B7U540）属于Kir2.x亚家族内向整流钾通道。其结构域包括细胞质N端、两个跨膜螺旋（M1和M2）、P-环（K+选择性过滤器）和大型C端胞质域（IRK_C IPR041647, IRK_N IPR013673），辅以Ig_E-set（IPR014756）结构域。Kir通道的生理特征为允许K+内流远超外流（内向整流），由胞内Mg2+和多胺的电压依赖性阻断介导。KCNJ18在甲状腺毒性周期性瘫痪（TPP）中发挥关键作用——甲状腺激素通过cAMP/PKA信号增强Kir2.6的表达和活性，导致K+内流增加和膜电位过极化（PMIDs:39333966, 40434516, 41800133）。

**核质K+浓度与染色质动力学的物理化学耦合**：核内K+浓度（~140 mM）是染色质纤维压缩的关键物理化学参数。高K+浓度屏蔽DNA磷酸骨架的负电荷，降低核小体间的静电排斥，促进异染色质凝聚。离子通道的核质定位（Nucleoplasm Supported，核定位特异性7/10）若为功能性（即在内核膜上形成功能性K+通道），则可局部调控核质K+微域，影响着丝粒周围异染色质和核纤层相关染色质域（LADs）的压缩状态——LADs区域的TE（LINE-1, ERV）通常在核纤层处被异染色质化沉默。若KCNJ18影响局部K+浓度进而改变异染色质物理特性，则间接影响LAD-TE的沉默稳定性。

**Ig_E-set结构域与可能的蛋白-蛋白互作功能**：KCNJ18的N端Ig_E-set（IPR014756, 免疫球蛋白E-set折叠）在Kir家族中独特，其可能介导同源或异源Kir通道亚基组装（如与KCNJ2/Kir2.1或KCNJ5/Kir3.4的异源四聚化）。Ig样折叠也常见于细胞粘附分子和免疫检查点——IGSF11（第27号候选）的两个Ig_V-set结构域为本批次中的平行实例。PPI degree=15（含EMD和KCNJ2/KCNJ5）的低互作度反映了Kir通道的亚基组装特异性。

**不确定性核定位与TPP的TE表达**：HPA核质定位为Uncertain级别（7/10）——在三个细胞系中的不一致性（某些U2OS细胞中核信号可能为过表达伪影）。AlphaFold pLDDT=80.6的中等置信度和PDB=0的结构缺失需实验结构补充。TPP中甲状腺激素的核受体（TRα/β）直接结合于HERV和MER4中的甲状腺激素应答元件（TRE），调控TE的转录激活——KCNJ18的核定位若伴随TR信号，可能构成K+通道-TR-TE调控的协同轴。归一化得分68.3/100。


### 补充分析 (UniProt API)

**蛋白全称**: Inward rectifier potassium channel 18

**功能**: Inward rectifier potassium channels are characterized by a greater tendency to allow potassium to flow into the cell rather than out of it. Their voltage dependence is regulated by the concentration of extracellular potassium; as external potassium is raised, the voltage range of the channel opening shifts to more positive voltages. The inward rectification is mainly due to the blockage of outward current by internal magnesium

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR014756 |
| InterPro | IPR041647 |
| InterPro | IPR016449 |
| InterPro | IPR003272 |
| InterPro | IPR013518 |
| InterPro | IPR013673 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| EMD | BioGRID | 0 |
| KCNJ2 | BioGRID | 0 |
| KCNJ5 | BioGRID | 0 |