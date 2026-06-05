---
type: protein-evaluation
gene: "JADE2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## JADE2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | JADE2 / JADE2|PHF15|KIAA1826|FLJ14719|MGC129797 |
| 蛋白全称 | E3 ubiquitin-protein ligase Jade-2 |
| 蛋白大小 | 790 aa / ~86.9 kDa |
| UniProt ID |  |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/JADE2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/JADE2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | 核为主：UniProt Nucleus + GO 支持 |
| 蛋白大小 | 8/10 | x1 | 8 | 790 aa，适宜 |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed 14 篇 |
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
| GeneCards | Nucleus (GO-CC) | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus (GO-CC) | — |
| GO Cellular Component | extracellular exosome | histone acetyltransferase complex | nucleoplasm | — |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 蛋白大小评估

**评价**: 790 aa (~86.9 kDa)，适合常规生化实验和结构解析，大小接近理想范围（200–800 aa）。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 14 |
| 新颖性评级 | 极度新颖 |

**主要研究方向**:
- E3 ubiquitin-protein ligase Jade-2 的功能研究
- 转录调控/信号传导相关

**评价**: PubMed 14 篇，几乎未被研究，属于极度新颖的蛋白。

**关键文献**:
1. Gaurav N et al. (2024). "Guiding the HBO1 complex function through the JADE subunit". *Nat Struct Mol Biol*. PMID: 38448574
2. Turk A et al. (2025). "Increased burden of rare variants in GWAS associated genes in familial multiple sclerosis". *Sci Rep*. PMID: 40592943
3. Munir M et al. (2023). "Genome-wide CRISPR activation screen identifies JADE3 as an antiviral activator of NF-kB". *bioRxiv*. PMID: 37808733
4. Xiao S et al. (2024). "Analysis of immune cell infiltration characteristics in severe acute pancreatitis through integrated bioinformatics". *Sci Rep*. PMID: 38622245
5. Fan M et al. (2022). "JADE2 Is Essential for Hippocampal Synaptic Plasticity and Cognitive Functions in Mice". *Biol Psychiatry*. PMID: 36008159
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 全局 pLDDT | 61.81 |
| pLDDT > 90 占比 | 22% |
| pLDDT > 70 占比 | 44% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 0 个 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/JADE2/JADE2-PAE.png]]

**评价**: 新颖蛋白基线 (6/10)。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt InterPro | Enhancer_polycomb-like_N, EPHD, Histone_Mod_Regulator, JADE2_ePHD, JADE2_PHD, Zinc_finger_PHD-type_CS, Znf_FYVE_PHD, Znf_PHD |
| Pfam | EPL1, PHD_2, zf-HC5HC2H_2 |

**染色质调控潜力分析**: 包含明确的 DNA 结合/染色质调控结构域：EPHD, Histone_Mod_Regulator, JADE2_ePHD, JADE2_PHD, Zinc_finger_PHD-type_CS, Znf_FYVE_PHD, Znf_PHD

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ING4 | 0.874 | — | — |
| KAT7 | 0.839 | — | — |
| MEAF6 | 0.799 | — | — |
| ING5 | 0.861 | — | — |
| ING3 | 0.592 | — | — |


**已知复合体成员** (GO Cellular Component):
- histone acetyltransferase complex

**PPI 互证分析**:
- 物理互作证据：IntAct 有实验互作数据
- STRING 预测：23 个 partner，>0.7 高置信度有
- 调控相关比例：需进一步验证

**评价**: STRING 预测互作，调控因子部分 (4/10)。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=61.81, PDB=0个 | — |
| 结构域 | InterPro / Pfam / SMART | Enhancer_polycomb-like_N, EPHD, Histone_Mod_Regulator, JADE2_ePHD, JADE2_PHD, Zi | — |
| PPI | STRING + IntAct | 有网络 | — |
| 定位 | UniProt / GO | Nucleus (GO-CC) | — |

**互证加分明细**: 无额外互证加分。

### 4. 总体评价

**推荐等级**: ★★★☆☆ (74.3/100)

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
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=JADE2
- STRING: https://string-db.org/network/9606.ENSP00000000
- IntAct: https://www.ebi.ac.uk/intact/search?query=JADE2


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[JADE2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/JADE2/JADE2-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000043143-JADE2/subcellular

![](https://images.proteinatlas.org/25959/258_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/25959/258_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/25959/259_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/25959/259_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/25959/260_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/25959/260_E4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
