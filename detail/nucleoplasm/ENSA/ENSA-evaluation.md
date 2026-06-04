---
type: protein-evaluation
gene: "ENSA"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ENSA 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ENSA / ARPP-19e |
| 蛋白名称 | Alpha-endosulfine |
| UniProt ID | O43768 |
| 蛋白大小 | 121 aa |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA Nucleoplasm + GO nucleoplasm, nuc=4 |
| 蛋白大小 | 8/10 | ×1 | 8 | 121 aa (偏小) |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 80 篇 (51-100) |
| 三维结构 | 6/10 | ×3 | 18 | AF pLDDT=67.4, 46%有序, 无PDB |
| 调控结构域 | 7/10 | ×2 | 14 | Endosulphine 家族, 无DNA结合域 |
| PPI 网络 | 5/10 | ×3 = 15 | MASTL/PPP2R2D 磷酸酶调控 |
| 互证加分 | — | max +3 | +0.5 | GO nucleoplasm + 磷酸酶通路 |
| **原始总分** |  |  | **99.5/183** |  |
| **归一化总分** |  |  | **54.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|------|------|--------|
| TEreg 筛选 | 核评分 4 | Tier1 |
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm | Reviewed |
| GO-Cellular Component | Nucleoplasm | IEA |


**HPA IF 图像**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ENSA/IF_images/116887_A_7_4_rna_selected.jpg|HPA IF]]

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ENSA/IF_images/116887_A_8_3_rna_selected.jpg|HPA IF]]

**结论**: HPA 显示核质定位，但 UniProt 注释为 Cytoplasm。核评分仅 4，核定位证据相对较弱。

#### 3.2 蛋白大小评估
**评价**: 121 aa，偏小但结构紧凑。Endosulfine 家族的小蛋白。

#### 3.3 研究现状
| 指标 | 数值 |
|------|------|
| PubMed 总数 | 80 |
| 主要研究方向 | 蛋白磷酸酶 2A 抑制, 有丝分裂调控 |

**主要研究方向**:
- PP2A 蛋白磷酸酶的内源性抑制因子
- MASTL-ENSA-PP2A 有丝分裂调控通路
- 胰岛素分泌调节

**关键文献**:
1. Gharbi-Ayachi et al. (2010). "ENSA/ARPP19 as PP2A inhibitors". PMID: 20864034
2. Mochida et al. (2010). "Greatwall phosphorylates ENSA". PMID: 21164014
3. Heron-Milhavet et al. (2006). "ENSA in insulin secretion". PMID: 16530266

**评价**: 研究适中（80篇），以有丝分裂 PP2A 调控为核心。与核蛋白的直接关联有限。

#### 3.4 三维结构分析
| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| 平均 pLDDT | 67.4 |
| 有序区域 (pLDDT>70) 占比 | 46% |
| 可用 PDB 条目 | 无 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ENSA/ENSA-PAE.png]]

**评价**: AF 预测中等质量，约一半为有序折叠。无 PDB 实验结构。

#### 3.5 结构域分析
| 来源 | 结构域 |
|------|--------|
| InterPro | Endosulphine (IPR006760) |
| Pfam | Endosulfine |

**染色质调控潜力分析**: 无 DNA 结合或染色质调控结构域。功能为 PP2A 内源性抑制因子。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作**:
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| MASTL | 0.99 | Greatwall 激酶 | 否 |
| PPP2R2D | 0.99 | PP2A 调节亚基 | 否 |
| MINK1 | 0.90 | 激酶 | 否 |
| PPP2R1A | 0.89 | PP2A 支架亚基 | 否 |
| PPP2CA | 0.86 | PP2A 催化亚基 | 否 |

**已知复合体成员** (GO Cellular Component): Nucleoplasm

**评价**: PPI 以磷酸酶/激酶通路为主，与转录调控关联有限。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| PPI | STRING PP2A 通路 | MASTL-PP2A | 一致 |
| 定位 | HPA Nucleoplasm vs UniProt Cytoplasm | 不一致 | 不一致 |

**互证加分明细**:
- GO nucleoplasm 低证据 (+0.5)
- **总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: 2 / 5

**核心优势**:
1. 有丝分裂调控通路成员

**风险/不确定性**:
1. 核定位证据弱（UniProt 说 Cytoplasm）
2. 无 DNA 结合/染色质调控域
3. 主要功能为细胞质磷酸酶抑制

**下一步建议**:
- [ ] 独立验证核定位
- [ ] 评估核定位分数是否应下调

### 5. 数据来源
- UniProt: O43768 (https://www.uniprot.org/uniprotkb/O43768)
- AlphaFold: AF-O43768-F1 v6 (https://alphafold.ebi.ac.uk/entry/O43768)
- Protein Atlas: ENSA (https://www.proteinatlas.org/)
- PubMed: ENSA (https://pubmed.ncbi.nlm.nih.gov/)
- STRING: ENSA (https://string-db.org/)
- InterPro: O43768 (https://www.ebi.ac.uk/interpro/)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ENSA-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ENSA/ENSA-PAE.png]]




