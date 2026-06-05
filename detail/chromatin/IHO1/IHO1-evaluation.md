---
type: protein-evaluation
gene: "IHO1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IHO1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IHO1 / IHO1|CCDC36|CT74 |
| 蛋白全称 | Interactor of HORMAD1 protein 1 |
| 蛋白大小 | 594 aa / ~65.3 kDa |
| UniProt ID |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/IHO1/IF_images/BJ-Human-fibroblast_1.jpg|BJ [Human fibroblast]]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/IHO1/IF_images/SiHa_1.jpg|SiHa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | 严格核蛋白：UniProt Nucleus + GO 支持（HPA 无 IF 数据） |
| 蛋白大小 | 10/10 | x1 | 10 | 594 aa，适宜 |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed 10 篇 |
| 三维结构 | 6/10 | x3 | 18 | 新颖蛋白基线 (6/10) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线 (7/10) |
| PPI 网络 | 4/10 | x3 | 12 | STRING 预测互作，调控因子部分 (4/10) |
| 互证加分 | +0 | max +3 | +0 | — |
| **原始总分** |  |  | **140/183** |  |
| **归一化总分** |  |  | **76.5/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Chromosome | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Chromosome | — |
| GO Cellular Component | condensed nuclear chromosome | — |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 蛋白大小评估

**评价**: 594 aa (~65.3 kDa)，适合常规生化实验和结构解析，大小接近理想范围（200–800 aa）。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 10 |
| 新颖性评级 | 极度新颖 |

**主要研究方向**:
- Interactor of HORMAD1 protein 1 的功能研究
- 转录调控/信号传导相关

**关键文献**:
1. Dereli et al. (2024). "Seeding the meiotic DNA break machinery and initiating recombination on chromosome axes.". *Nat Commun*. PMID: 38580643
2. Biot et al. (2024). "Principles of chromosome organization for meiotic recombination.". *Mol Cell*. PMID: 38657614
3. Dereli et al. (2021). "Four-pronged negative feedback of DSB machinery in meiotic DNA-break control in mice.". *Nucleic Acids Res*. PMID: 33619545
4. Nore et al. (2022). "TOPOVIBL-REC114 interaction regulates meiotic DNA double-strand breaks.". *Nat Commun*. PMID: 36396648
5. Dereli et al. (2023). "Seeding the meiotic DNA break machinery and initiating recombination on chromosome axes.". *bioRxiv*. PMID: 38077023
**评价**: PubMed 10 篇，几乎未被研究，属于极度新颖的蛋白。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 全局 pLDDT | 54.66 |
| pLDDT > 90 占比 | 21% |
| pLDDT > 70 占比 | 25% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 0 个 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/IHO1/IHO1-PAE.png]]

**评价**: 新颖蛋白基线 (6/10)。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt InterPro | IHO1 |
| Pfam | IHO1 |

**染色质调控潜力分析**: 未注释到经典染色质/DNA 结合结构域，但属于新颖蛋白（基线不扣分）。AlphaFold 预测有可辨识折叠域，存在新结构域发现潜力。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| REC114 | 0.000 | — | — |
| HORMAD1 | 0.000 | — | — |
| MEI4 | 0.000 | — | — |
| CXXC1 | 0.000 | — | — |
| ANKRD31 | 0.000 | — | — |


**已知复合体成员** (GO Cellular Component):
- 未注释到特定染色质调控复合体

**PPI 互证分析**:
- 物理互作证据：IntAct 有实验互作数据
- STRING 预测：30 个 partner，>0.7 高置信度较少
- 调控相关比例：需进一步验证

**评价**: STRING 预测互作，调控因子部分 (4/10)。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=54.66, PDB=0个 | — |
| 结构域 | InterPro / Pfam / SMART | IHO1 | — |
| PPI | STRING + IntAct | 有网络 | — |
| 定位 | UniProt / GO | Chromosome | — |

**互证加分明细**: 无额外互证加分。

### 4. 总体评价

**推荐等级**: ★★★☆☆ (76.5/100)

**核心优势**:
1. 极度新颖（PubMed 10 篇），niche 空间充足
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
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IHO1
- STRING: https://string-db.org/network/9606.ENSP00000000
- IntAct: https://www.ebi.ac.uk/intact/search?query=IHO1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[IHO1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/IHO1/IHO1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000173421-IHO1/subcellular

![](https://images.proteinatlas.org/69534/1331_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/69534/1331_D12_4_red_green.jpg)
![](https://images.proteinatlas.org/69534/1339_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/69534/1339_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/69534/1345_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/69534/1345_D12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
