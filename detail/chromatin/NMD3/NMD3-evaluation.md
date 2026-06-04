---
type: protein-evaluation
gene: "NMD3"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NMD3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NMD3 / CGI-07 |
| 蛋白名称 | 60S ribosomal export protein NMD3 |
| 蛋白大小 | 503 aa |
| UniProt ID | Q96D46 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/NMD3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/NMD3/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | **28** | UniProt Nucleus + 部分胞质 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 503 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 26篇，非常新颖 |
| 🏗️ 三维结构 | 8/10 | ×3 | **24** | 3 个 PDB 实验结构 + AlphaFold 预测 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 7 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+2.0** | 核定位: UniProt + GO 双库一致 (+1); 三维结构: AlphaFold + PDB 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
| **原始总分** |  |  | **129/183** |  |
| **归一化总分** |  |  | **70.5/100** |  |

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

**评价**: 503 aa，503 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 26 |
| 核定位分数 (weighted max) | 6 |
| Research hotness | 4.1631 |

**关键文献**:
1. Lo et al. (2009). "Reengineering ribosome export.". *Mol Biol Cell*. PMID: 19144820
2. Wang et al. (2024). "RNA-binding protein hnRNPU regulates multiple myeloma resistance to selinexor.". *Cancer Lett*. PMID: 37984724
3. Oeffinger et al. (2010). "Joining the interface: a site for Nmd3 association on 60S ribosome subunits.". *J Cell Biol*. PMID: 20584913
4. Kargas et al. (2019). "Mechanism of completion of peptidyltransferase centre assembly in eukaryotes.". *Elife*. PMID: 31115337
5. Johnson et al. (2002). "Nuclear export of ribosomal subunits.". *Trends Biochem Sci*. PMID: 12417134
**评价**: PubMed 26篇，非常新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 503 aa |
| PDB 条目数 | 3 |
| UniProt 注释结构域数 | 7 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/NMD3/NMD3-PAE.png]]

**评价**: 3 个 PDB 实验结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | Nmd3 |
| InterPro | Nmd3_N |
| InterPro | NMD_SH3 |
| InterPro | OB_NMD3 |
| Pfam | NMD3 |
| Pfam | NMD_SH3 |
| Pfam | OB_NMD3 |

**染色质调控潜力分析**: 7 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| LSG1 | 0 |  | 否 |
| PA2G4 | 0 |  | 否 |
| RSL24D1 | 0 |  | 否 |
| GTPBP4 | 0 |  | 否 |
| EIF6 | 0 |  | 否 |
| XPO1 | 0 |  | 否 |
| GNL2 | 0 |  | 否 |
| RPL5 | 0 |  | 否 |
| ZNF622 | 0 |  | 否 |
| ZNF593 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

—

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 3 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 7 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
核定位: UniProt + GO 双库一致 (+1)
三维结构: AlphaFold + PDB 双源 (+0.5)
结构域: 多库注释一致 (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 26 篇，比较新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 无 HPA IF 实验数据
2. 3 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NMD3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169251-NMD3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NMD3%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96D46
- STRING: https://string-db.org/network/9606.ENSG00000169251
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96D46


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NMD3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/NMD3/NMD3-PAE.png]]


