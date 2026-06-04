---
type: protein-evaluation
gene: "NOSIP"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NOSIP 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NOSIP / CGI-25 |
| 蛋白名称 | Nitric oxide synthase-interacting protein |
| 蛋白大小 | 301 aa |
| UniProt ID | Q9Y314 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NOSIP/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NOSIP/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | **28** | UniProt Nucleus + 部分胞质 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 301 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 31篇，非常新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 2 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 10/10 | ×2 | **20** | 明确染色质/DNA 调控结构域: znf_ring/fyve/phd |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.5** | 核定位: UniProt + GO 双库一致 (+1); 三维结构: AlphaFold + PDB 双源 (+0.5) |
| **原始总分** |  |  | **135/183** |  |
| **归一化总分** |  |  | **73.8/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Cytoplasm, Nucleus | 实验/预测 |
| GO Cellular Component | N/A | N/A |

**结论**: UniProt Nucleus + 部分胞质

#### 3.2 蛋白大小评估

**评价**: 301 aa，301 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 31 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 4.6405 |

**关键文献**:
1. Pörschke et al. (2023). "Transportin 1 is a major nuclear import receptor of the nitric oxide synthase interacting protein.". *J Biol Chem*. PMID: 36690276
2. Dreyer et al. (2004). "Nitric oxide synthase (NOS)-interacting protein interacts with neuronal NOS and regulates its distribution and activity.". *J Neurosci*. PMID: 15548660
3. Gao et al. (2023). "Nosip is a potential therapeutic target in hepatocellular carcinoma cells.". *iScience*. PMID: 37529099
4. Hoffmeister et al. (2017). "Developmental neurogenesis in mouse and Xenopus is impaired in the absence of Nosip.". *Dev Biol*. PMID: 28663132
5. Hoffmeister et al. (2014). "The ubiquitin E3 ligase NOSIP modulates protein phosphatase 2A activity in craniofacial development.". *PLoS One*. PMID: 25546391
**评价**: PubMed 31篇，非常新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 301 aa |
| PDB 条目数 | 2 |
| UniProt 注释结构域数 | 4 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NOSIP/NOSIP-PAE.png]]

**评价**: 2 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | NOSIP |
| InterPro | Znf-NOSIP |
| InterPro | Znf_RING/FYVE/PHD |
| Pfam | zf-NOSIP |

**染色质调控潜力分析**: 明确染色质/DNA 调控结构域: znf_ring/fyve/phd

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| NOS3 | 0 |  | 否 |
| SNRNP40 | 0 |  | 否 |
| NOSTRIN | 0 |  | 否 |
| NOS1 | 0 |  | 否 |
| CAV1 | 0 |  | 否 |
| DNM2 | 0 |  | 否 |
| C9orf78 | 0 |  | 否 |
| PGS1 | 0 |  | 否 |
| PRRG2 | 0 |  | 否 |
| HSP90AA1 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

—

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 2 entries | 一致 |
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
1. 新颖性: PubMed 31 篇，比较新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 2 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NOSIP
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142546-NOSIP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NOSIP%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9Y314
- STRING: https://string-db.org/network/9606.ENSG00000142546
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y314


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NOSIP-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/NOSIP/NOSIP-PAE.png]]


