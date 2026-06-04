---
type: protein-evaluation
gene: "NPM2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NPM2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NPM2 / — |
| 蛋白名称 | Nucleoplasmin-2 |
| 蛋白大小 | 214 aa |
| UniProt ID | Q86SE8 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NPM2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NPM2/IF_images/Hep-G2_1.jpg|Hep-G2]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus，中等可信度 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 214 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 44篇，非常新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 4 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.5** | 核定位: UniProt + GO 双库一致 (+1); 三维结构: AlphaFold + PDB 双源 (+0.5) |
|  | **原始总分** |  | **123/183** | **122.0/183** |  |
|  | **归一化总分** |  | **67.2/100** | **66.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus | 实验/预测 |
| GO Cellular Component | N/A | N/A |

**结论**: UniProt Nucleus，中等可信度

#### 3.2 蛋白大小评估

**评价**: 214 aa，214 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 44 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 3.6622 |

**关键文献**:
1. Gou et al. (2020). "Initiation of Parental Genome Reprogramming in Fertilized Oocyte by Splicing Kinase SRPK1-Catalyzed Protamine Phosphorylation.". *Cell*. PMID: 32169215
2. Wu et al. (2022). "NPM2 in malignant peritoneal mesothelioma: from basic tumor biology to clinical medicine.". *World J Surg Oncol*. PMID: 35490253
3. Vitale et al. (2007). "Proteomic profiling of murine oocyte maturation.". *Mol Reprod Dev*. PMID: 17044029
4. Chen et al. (2019). "Nucleoplasmin is a limiting component in the scaling of nuclear size with cytoplasmic volume.". *J Cell Biol*. PMID: 31636119
5. Burns et al. (2003). "Roles of NPM2 in chromatin and nucleolar organization in oocytes and embryos.". *Science*. PMID: 12714744
**评价**: PubMed 44篇，非常新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 214 aa |
| PDB 条目数 | 1 |
| UniProt 注释结构域数 | 4 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NPM2/NPM2-PAE.png]]

**评价**: 1 个 PDB 实验结构 + AlphaFold 预测

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
| NPM3 | 0 |  | 否 |
| NPM1 | 0 |  | 否 |
| NCL | 0 |  | 否 |
| KPNA7 | 0 |  | 否 |
| ZAR1 | 0 |  | 否 |
| H2AC18 | 0 |  | 否 |
| H2AC20 | 0 |  | 否 |
| H2BC21 | 0 |  | 否 |
| NOP58 | 0 |  | 否 |
| ALK | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

- C:chromatin (GO:0000785, IDA:UniProtKB)
- F:chromatin binding (GO:0003682, IBA:GO_Central)
- P:chromatin remodeling (GO:0006338, IDA:UniProtKB)

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 4 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
三维结构: AlphaFold + PDB 双源 (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 44 篇，比较新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 1 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NPM2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158806-NPM2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NPM2%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q86SE8
- STRING: https://string-db.org/network/9606.ENSG00000158806
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86SE8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NPM2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/NPM2/NPM2-PAE.png]]


