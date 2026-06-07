---
type: protein-evaluation
gene: "ICE2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ICE2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ICE2 / ICE2|NARG2|RBAF602|C15orf17 |
| 蛋白全称 | Little elongation complex subunit 2 |
| 蛋白大小 | 982 aa / ~108.0 kDa |
| UniProt ID |  |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ICE2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ICE2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | 核为主：UniProt Nucleus + GO 支持 |
| 蛋白大小 | 8/10 | x1 | 8 | 982 aa，适宜 |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed 14 篇 |
| 三维结构 | 6/10 | x3 | 18 | 新颖蛋白基线 (6/10) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线 (7/10) |
| PPI 网络 | 2/10 | x3 | 6 | 互作数据有限 (2/10) |
| 互证加分 | +0 | max +3 | +0 | — |
| **原始总分** |  |  | **124/183** |  |
| **归一化总分** |  |  | **67.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus | — |
| GO Cellular Component | Cajal body | cytosol | euchromatin | histone locus body | nuclear body | nucleoplasm | — |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 蛋白大小评估

**评价**: 982 aa (~108.0 kDa)，大小偏大，可能增加实验难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 14 |
| 新颖性评级 | 极度新颖 |

**主要研究方向**:
- Little elongation complex subunit 2 的功能研究
- 转录调控/信号传导相关

**评价**: PubMed 14 篇，几乎未被研究，属于极度新颖的蛋白。

**关键文献**:
1. Pantalon AD et al. (2020). "Outcomes of phacoemulsification combined with two iStent inject trabecular microbypass stents with or without endocyclophotocoagulation". *Br J Ophthalmol*. PMID: 31980421
2. Kim YS et al. (2015). "The unified ICE-CBF pathway provides a transcriptional feedback control of freezing tolerance during cold acclimation in Arabidopsis". *Plant Mol Biol*. PMID: 26311645
3. Kurbidaeva A et al. (2014). "Arabidopsis thaliana ICE2 gene: phylogeny, structural evolution and functional diversification from ICE1". *Plant Sci*. PMID: 25443829
4. Papagiannidis D et al. (2021). "Ice2 promotes ER membrane biogenesis in yeast by inhibiting the conserved lipin phosphatase complex". *EMBO J*. PMID: 34617598
5. Bai R et al. (2021). "Identification of prognostic lipid droplet-associated genes in pancreatic cancer patients via bioinformatics analysis". *Lipids Health Dis*. PMID: 34078402
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 全局 pLDDT | 65.19 |
| pLDDT > 90 占比 | 29% |
| pLDDT > 70 占比 | 52% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 0 个 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ICE2/ICE2-PAE.png]]

**评价**: 新颖蛋白基线 (6/10)。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt InterPro | ICE2_C |
| Pfam | NARG2_C |

**染色质调控潜力分析**: 未注释到经典染色质/DNA 结合结构域，但属于新颖蛋白（基线不扣分）。AlphaFold 预测有可辨识折叠域，存在新结构域发现潜力。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ICE1 | 0.292 | — | — |
| ZC3H8 | 0.000 | — | — |
| ELL | 0.328 | — | — |
| EAF1 | 0.525 | — | — |
| ELL3 | 0.559 | — | — |


**已知复合体成员** (GO Cellular Component):
- Cajal body | euchromatin | histone locus body | nuclear body | transcription elongation factor complex

**PPI 互证分析**:
- 物理互作证据：IntAct 有实验互作数据
- STRING 预测：30 个 partner，>0.7 高置信度较少
- 调控相关比例：需进一步验证

**评价**: 互作数据有限 (2/10)。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=65.19, PDB=0个 | — |
| 结构域 | InterPro / Pfam / SMART | ICE2_C | — |
| PPI | STRING + IntAct | 有网络 | — |
| 定位 | UniProt / GO | Nucleus | — |

**互证加分明细**: 无额外互证加分。

### 4. 总体评价

**推荐等级**: ★★★☆☆ (67.8/100)

**核心优势**:
1. 极度新颖（PubMed 14 篇），niche 空间充足
2. 核为主：UniProt Nucleus + GO 支持
3. 新颖蛋白基线 (6/10)

**风险/不确定性**:
1. HPA IF 数据缺失，核定位待实验验证
2. PPI 数据有限，调控网络待探索
3. 功能研究较少，生物学角色待阐明

**下一步建议**:
- [ ] 获取 HPA IF 数据或多重 IF 验证核定位
- [ ] Co-IP/MS 鉴定互作伙伴
- [ ] ChIP-seq 分析基因组结合位点（如为 TF/染色质蛋白）

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ICE2
- STRING: https://string-db.org/network/9606.ENSP00000000
- IntAct: https://www.ebi.ac.uk/intact/search?query=ICE2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ICE2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ICE2/ICE2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000128915-ICE2/subcellular

![](https://images.proteinatlas.org/40058/2269_G4_116_red_green.jpg)
![](https://images.proteinatlas.org/40058/2269_G4_88_red_green.jpg)
![](https://images.proteinatlas.org/40058/412_F11_3_red_green.jpg)
![](https://images.proteinatlas.org/40058/412_F11_4_red_green.jpg)
![](https://images.proteinatlas.org/40058/419_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/40058/419_F11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q659A1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019535; |
| Pfam | PF10505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000128915-ICE2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ELL | Intact, Biogrid | true |
| ICE1 | Intact, Biogrid | true |
| DIS3 | Bioplex | false |
| EAF1 | Biogrid | false |
| EMG1 | Bioplex | false |
| HARS2 | Bioplex | false |
| IDH3G | Bioplex | false |
| LETM1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
