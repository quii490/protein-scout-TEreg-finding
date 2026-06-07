---
type: protein-evaluation
gene: "IRX6"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IRX6 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IRX6 / IRX6|IRX3|IRXB3 |
| 蛋白全称 | Iroquois-class homeodomain protein IRX-6 |
| 蛋白大小 | 446 aa / ~49.1 kDa |
| UniProt ID |  |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IRX6/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IRX6/IF_images/SK-MEL-30_1.jpg|SK-MEL-30]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | 严格核蛋白：UniProt Nucleus + GO 支持（HPA 无 IF 数据） |
| 蛋白大小 | 10/10 | x1 | 10 | 446 aa，适宜 |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed 29 篇 |
| 三维结构 | 6/10 | x3 | 18 | 新颖蛋白基线 (6/10) |
| 调控结构域 | 10/10 | x2 | 20 | 明确 chromatin/DNA-binding 结构域 |
| PPI 网络 | 4/10 | x3 | 12 | STRING 预测互作，调控因子部分 (4/10) |
| 互证加分 | +0 | max +3 | +0 | — |
| **原始总分** |  |  | **136/183** |  |
| **归一化总分** |  |  | **74.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus | — |
| Protein Atlas (IF) | IF image available (embedded above) | See IF_images/ |
| UniProt | Nucleus | — |
| GO Cellular Component | chromatin | nucleus | — |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 蛋白大小评估

**评价**: 446 aa (~49.1 kDa)，适合常规生化实验和结构解析，大小接近理想范围（200–800 aa）。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 29 |
| 新颖性评级 | 非常新颖 |

**主要研究方向**:
- Iroquois-class homeodomain protein IRX-6 的功能研究
- 转录调控/信号传导相关

**评价**: PubMed 29 篇，研究较少，属于非常新颖的蛋白。

**关键文献**:
1. Ngoh A et al. (2025). "Clinical and Molecular Genetic Characterization of Landau Kleffner Syndrome: An Observational Cohort and Experimental Study". *Ann Neurol*. PMID: 40944498
2. Xue JY et al. (2024). "COBRA-LIKE4 modulates cellulose synthase velocity and facilitates cellulose deposition in the secondary cell wall". *Plant Physiol*. PMID: 39230913
3. Catela C et al. (2024). "The Iroquois (Iro/Irx) homeobox genes are conserved Hox targets involved in motor neuron development". *bioRxiv*. PMID: 38853975
4. Mummenhoff J et al. (2001). "Expression of Irx6 during mouse morphogenesis". *Mech Dev*. PMID: 11335133
5. Nagel S (2023). "The Role of IRX Homeobox Genes in Hematopoietic Progenitors and Leukemia". *Genes (Basel)*. PMID: 36833225
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 全局 pLDDT | 54.53 |
| pLDDT > 90 占比 | 10% |
| pLDDT > 70 占比 | 13% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 0 个 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IRX6/IRX6-PAE.png]]

**评价**: 新颖蛋白基线 (6/10)。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt InterPro | HD, Homeobox_CS, Homeodomain-like_sf, Iroquois_homeo, KN_HD |
| Pfam | Homeobox_KN |

**染色质调控潜力分析**: 包含明确的 DNA 结合/染色质调控结构域：Homeobox_CS, Homeodomain-like_sf

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| FTO | 0.000 | — | — |
| NKX2-2 | 0.072 | — | — |
| SIX3 | 0.000 | — | — |
| OLIG2 | 0.050 | — | — |
| RPGRIP1L | 0.069 | — | — |


**已知复合体成员** (GO Cellular Component):
- chromatin

**PPI 互证分析**:
- 物理互作证据：IntAct 有实验互作数据
- STRING 预测：30 个 partner，>0.7 高置信度较少
- 调控相关比例：需进一步验证

**评价**: STRING 预测互作，调控因子部分 (4/10)。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=54.53, PDB=0个 | — |
| 结构域 | InterPro / Pfam / SMART | HD, Homeobox_CS, Homeodomain-like_sf, Iroquois_homeo, KN_HD | — |
| PPI | STRING + IntAct | 有网络 | — |
| 定位 | UniProt / GO | Nucleus | — |

**互证加分明细**: 无额外互证加分。

### 4. 总体评价

**推荐等级**: ★★★☆☆ (74.3/100)

**核心优势**:
1. 研究新颖（PubMed 29 篇）
2. 严格核蛋白：UniProt Nucleus + GO 支持（HPA 无 IF 数据）
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
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IRX6
- STRING: https://string-db.org/network/9606.ENSP00000000
- IntAct: https://www.ebi.ac.uk/intact/search?query=IRX6


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[IRX6-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IRX6/IRX6-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000159387-IRX6/subcellular

![](https://images.proteinatlas.org/18332/1639_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18332/1639_D1_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/18332/1682_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18332/1682_A2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P78412 |
| SMART | SM00389;SM00548; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR017970;IPR009057;IPR003893;IPR008422; |
| Pfam | PF05920; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000159387-IRX6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARID5A | Intact | false |
| CRX | Intact | false |
| GLRX3 | Intact | false |
| KRTAP19-7 | Intact | false |
| MYL2 | Intact | false |
| NFKBID | Intact | false |
| PFDN5 | Intact | false |
| TBX19 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
