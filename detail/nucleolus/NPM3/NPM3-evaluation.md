---
type: protein-evaluation
gene: "NPM3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NPM3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NPM3 / — |
| 蛋白名称 | Nucleoplasmin-3 |
| 蛋白大小 | 178 aa |
| UniProt ID | O75607 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NPM3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NPM3/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 8/10 | ×1 | **8** | 178 aa，可接受范围 |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 51篇，有一定研究空间 |
| 🏗️ 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 4 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.0** | 核定位: UniProt + GO 双库一致 (+1) |
| **原始总分** |  |  | **115/183** |  |
| **归一化总分** |  |  | **62.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus, Nucleus, nucleolus | 实验/预测 |
| GO Cellular Component | N/A | N/A |

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 178 aa，178 aa，可接受范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 51 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 5.2638 |

**关键文献**:
1. Gu et al. (2023). "SET7/9-mediated methylation affects oncogenic functions of histone demethylase JMJD2A.". *JCI Insight*. PMID: 37870957
2. Wang et al. (2024). "Pumilio1 regulates NPM3/NPM1 axis to promote PD-L1-mediated immune escape in gastric cancer.". *Cancer Lett*. PMID: 38029539
3. Xu et al. (2026). "NPM3 functions as a lactyltransferase to promote necroptosis in male diabetic cardiomyopathy mice models via FASN transcription modulation.". *Nat Commun*. PMID: 41803151
4. Chen et al. (2024). "NPM3 as an Unfavorable Prognostic Biomarker Involved in Oncogenic Pathways of Lung Adenocarcinoma via MYC Translational Activation.". *Comb Chem High Throughput Screen*. PMID: 37114782
5. Sun et al. (2025). "DCN, NPM3 and SULF1 are hub genes related to vasculogenic mimicry in lung adenocarcinoma.". *J Cancer Res Clin Oncol*. PMID: 41205056
**评价**: PubMed 51篇，有一定研究空间

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 178 aa |
| PDB 条目数 | 0 |
| UniProt 注释结构域数 | 4 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NPM3/NPM3-PAE.png]]

**评价**: 无 PDB 结构，AlphaFold 预测可用，新颖蛋白基线分

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | Nucleoplasmin |
| InterPro | Nucleoplasmin_core_dom |
| InterPro | Nucleoplasmin_core_dom_sf |
| Pfam | Nucleoplasmin |

**染色质调控潜力分析**: 4 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| NPM1 | 0 |  | 否 |
| NPM2 | 0 |  | 否 |
| OGA | 0 |  | 否 |
| FGF8 | 0 |  | 否 |
| NCL | 0 |  | 否 |
| NEPRO | 0 |  | 否 |
| RECQL4 | 0 |  | 否 |
| TMEM167A | 0 |  | 否 |
| H2AC18 | 0 |  | 否 |
| H2AC20 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

- F:chromatin binding (GO:0003682, IBA:GO_Central)
- P:chromatin remodeling (GO:0006338, IBA:GO_Central)

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 entries | 仅预测 |
| 结构域 | UniProt / InterPro / Pfam | 4 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★☆☆ (3/5)

**核心优势**:
1. 新颖性: PubMed 51 篇，有一定研究空间
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 无 PDB 实验结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: AlphaFold 预测为基础，设计突变实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NPM3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107833-NPM3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NPM3%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/O75607
- STRING: https://string-db.org/network/9606.ENSG00000107833
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75607


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NPM3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/NPM3/NPM3-PAE.png]]


