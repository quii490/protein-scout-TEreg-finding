---
type: protein-evaluation
gene: "AEBP1"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AEBP1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | AEBP1 / ACLP, AE-binding protein 1 |
| 蛋白大小 | 1158 aa / 130.9 kDa |
| UniProt ID | Q8IUX7 (canonical); Q8IUX7-2 (nuclear isoform) |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4 | /10 | ×3 = 12 | Isoform 1 secreted; isoform 2 nuclear. PA: mainly vesicles + nucleoplasm |
| 蛋白大小 | 8 | /10 | ×2 = 16 | 1158 aa, 130.9 kDa |
| 研究新颖性 | 8 | /10 | ×3 = 24 | PubMed narrow: 178, broad: 199 |
| 三维结构 | 5 | /10 | ×3 = 15 | Mean pLDDT 67.84; 53.2% >= 70; PAE mean 22.02 |
| 调控结构域 | 4 | /10 | ×2 = 8 | F5/8 type C + Peptidase M14 (enzymatic); GO DNA-binding repressor |
| 🔗 PPI | 0/10 | ×3 | **0** | 详见 3.6 PPI 分析 |
| 互证加分 | +0.5 | max +3 | +0.5 | 定位: UniProt + GO + PA 一致 |
| **原始总分** | | | **80.5/158** | |
| **归一化总分** | | | **50.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Region:Disordered(1-69) |
|---|---|
| UniProt | Secreted (isoform 1), Cytoplasm, Nucleus (isoform 2) | ECO evidence | Protein Atlas (IF) | Mainly vesicles; additionally nucleoplasm + cytosol | Supported |
| GO | Cytoplasm, extracellular space, nucleus, ECM | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/AEBP1/IF_images/MCF7_HPA047724.jpg|MCF7_HPA047724]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/AEBP1/IF_images/U2OS_HPA047724.jpg|U2OS_HPA047724]]

**结论**: AEBP1 的 canonical isoform (Q8IUX7) 是分泌蛋白，主要定位于细胞外基质 (ECM)。Isoform 2 缺乏信号肽，定位于细胞核并具有 DNA 结合和转录抑制活性。Protein Atlas IF 显示蛋白主要在囊泡中，核质有额外信号但非主要定位。这是一个以 ECM 功能为主的蛋白，核定位功能为次要/选择性剪接产物，不是理想的核蛋白研究对象。

**IF 图像**:

#### 3.2 蛋白大小评估
**评价**: 1158 aa 处于 800-1200 的适中范围，适合常规生化实验。但蛋白大部分区域为无序区 (residues 1-387, 1108-1141 disordered)，仅有约 47.7% 的残基具有高置信度折叠结构，这可能增加蛋白表达和纯化难度。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 (narrow) | 178 |
| PubMed 总数 (broad TIAB) | 199 |
| 最近研究方向 | ECM remodeling, collagen, Ehlers-Danlos syndrome, fibroblast biology |

**主要研究方向**:
- 胶原纤维组装与 ECM 重塑 (80%+)
- Ehlers-Danlos 综合征 classical-like type 2 (AEBP1 突变)
- 脂肪细胞增殖/分化调控
- 巨噬细胞炎症反应 (NF-kappaB)
- 转录抑制活性 (少数研究)

**评价**: 178 篇论文，研究集中于 ECM 和结缔组织疾病。转录调控方向有但极少，是研究空白。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 67.84 |
| PDB 实验结构 | — |
| 有序区域 (pLDDT>=70) 占比 | 53.2% |
| pLDDT>=90 占比 | 39.7% |
| pLDDT<50 占比 | 39.6% |
| 可用 PDB 条目 | 0 (仅有 AlphaFold 预测) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/AEBP1/AEBP1-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵尺寸: 1158 x 1158
- PAE 总体均值: 22.02
- PAE <5 A 占比: 11.84%; <10 A 占比: 22.61%
- 对角线均值: 0.00 (预期)

**评价**: 平均 pLDDT 67.84，处于中等水平。39.7% 的残基达到高置信度 (>=90)，主要集中于三个折叠域: (383-542) FA58C domain, (557-793) peptidase domain (部分), (833-987)。但仍有 39.6% 为无序区域 (<50)。PAE 均值 22.02 较高，提示蛋白整体柔性大。无可用的实验结构。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro/Pfam | F5/8 type C (FA58C, discoidin-like) (383-540); Peptidase M14 (zinc carboxypeptidase) (563-904) |
| SMART | FA58C (SM00231); Zn_pept (SM00631) |
| UniProt | F5/8 type C domain; Peptidase M14; Disordered regions |
| GO (Molecular Function) | DNA-binding transcription repressor activity, RNA Pol II regulatory region DNA binding, zinc ion binding, calmodulin binding, carboxypeptidase activity, collagen binding |

**染色质调控潜力分析**: 该蛋白的两个已知结构域 (FA58C, Peptidase M14) 均为酶学/细胞粘附相关，与染色质调控无直接关联。但 GO 注释中包含 "DNA-binding transcription repressor activity" 和 "RNA polymerase II regulatory region sequence-specific DNA binding"，且 isoform 2 可在体外结合 DNA。DNA 结合区域 (390-555) 与 FA58C domain 部分重叠——这可能是 discoidin 样结构域的 moonlighting 功能，也可能是未被结构域数据库识别的新型 DNA 结合域。整体染色质调控潜力偏低。

#### 3.6 PPI :
| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| COL1A1 | 0.999 | Collagen | No |
| COL1A2 | 0.999 | Collagen | No |
| COL3A1 | 0.998 | Collagen | No |
| COL6A2 | 0.998 | Collagen | No |
| COL5A1 | 0.996 | Collagen | No |
| LUM | 0.999 | Proteoglycan, ECM | No |
| PCOLCE | 0.976 | Procollagen processing | No |
| COL6A3 | 0.994 | Collagen | No |
| COL14A1 | 0.799 | Collagen | No |
| BGN | 0.976 | Proteoglycan, ECM | No |
| COL12A1 | 0.861 | Collagen | No |
| THBS2 | 0.898 | ECM glycoprotein | No |
| PDGFRB | 0.767 | Receptor tyrosine kinase | No (signaling) |
| COL5A2 | 0.792 | Collagen | No |
| COL11A1 | 0.976 | Collagen | No |
| FKBP14 | 0.665 | ER chaperone | No |
| EFEMP2 | 0.726 | ECM protein | No |
| CHST14 | 0.979 | Sulfotransferase, ECM | No |
| POSTN | 0.802 | ECM, cell adhesion | No |
| TCF3 | 0.650 | Transcription factor (E2A) | **Yes** |

**UniProt 实验互作**:

| Partner | 来源 | 与调控相关？ |
|---|---|---|
| NFKBIA | UniProt (isoform 2) | **Yes** (NF-kB pathway) |
| MAPK1/MAPK3 | UniProt (isoform 2) | Maybe (signaling) |
| PTEN | UniProt (isoform 2) | Maybe (signaling) |
| GNG5 | UniProt (isoform 2) | No |

**PPI 互证**: 无法获取 humanPPI 数据 。STRING 和 UniProt 均提示 NFKBIA 和 MAPK1/3 互作，但与调控相关 partner 极少。

**调控相关比例**: ~1/20 (5%)

**评价**: PPI ，且分数较低 (<0.7)。不适合作为染色质调控蛋白研究。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold pLDDT + PDB | 无实验结构, AlphaFold 预测为中等质量 | N/A |
| 结构域 | UniProt / InterPro / Pfam / SMART | F5/8 type C + Peptidase M14 一致 | 一致 (酶学域) |
| 🔗 PPI | 0/10 | ×3 | **0** | 详见 3.6 PPI 分析 | STRING | ECM/胶原| 一致 (混合定位) |

**互证加分明细**:
- 定位互证: UniProt + GO + Protein Atlas 均确认核定位 (isoform 2 或附加定位) → **+0.5**
- 结构域互证: >=3 来源确认相同域 → +0.5。但域功能为酶学/ECM，非染色质调控 → 不计入功能一致性加分
- 三维结构: 无 PDB 实验结构 vs AlphaFold → 0
- PPI 互证: 无法获取 humanPPI → 0
- 进化保守性: 未评估 → 0

**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: 2/5 (不推荐作为核蛋白/染色质项目主要候选)

**核心优势**:
1. 存在核定位 isoform 2，具有明确的 DNA 结合和转录抑制活性
2. DNA 结合区域 (390-555) 与 FA58C domain 重叠，可能代表 discoidin domain 的新型 DNA 结合功能

**风险/不确定性**:
1. Canonical isoform 是分泌/ECM 蛋白，核功能为次要产物，Protein Atlas 也显示主要在囊泡——不是合格的"核蛋白"候选
2. 几乎无染色质/表观遗传方向的现有研究，PPI - STRING: https://string-db.org (API)
- InterPro: https://www.ebi.ac.uk/interpro/ (API)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IUX7
- - humanPPI: 无法访问

![[Projects/TEreg-finding/protein-interested/detail/rejected/AEBP1/AEBP1-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/AEBP1/AEBP1-PAE.png]]




