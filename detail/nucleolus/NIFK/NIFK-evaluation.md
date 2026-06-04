---
type: protein-evaluation
gene: "NIFK"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NIFK 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | NIFK / Nop15|Nopp34|hNIFK |
| 蛋白名称 | MKI67 FHA domain-interacting nucleolar phosphoprotein |
| 蛋白大小 | 293 aa |
| UniProt ID | Q9BYG3 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NIFK/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NIFK/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 加权 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | **24** | 核+胞质均衡，UniProt 支持核定位 |
| 📏 蛋白大小 | 10/10 | ×1 | **10** | 293 aa，适合生化实验和结构解析 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 30篇，非常新颖 |
| 🏗️ 三维结构 | 10/10 | ×3 | **30** | 25 个 PDB 实验结构，实验验证充分 |
| 🧬 调控结构域 | 7/10 | ×2 | **14** | 8 个结构域注释，新颖蛋白基线（存在新域发现潜力） |
| 🔗 PPI 网络 | 4/10 | ×3 | **12** | STRING 15 partners，调控比例较低 |
| ➕ 互证加分 | — | — | **+1.0** | 三维结构: AlphaFold + PDB 双源 (+0.5); 结构域: 多库注释一致 (+0.5) |
| **原始总分** |  |  | **130.5/183** |  |
| **归一化总分** |  |  | **71.3/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_conserved_high_confidence | 高置信度保守 |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus, nucleolus, Chromosome | 实验/预测 |
| GO Cellular Component | N/A | N/A |

**结论**: 核+胞质均衡，UniProt 支持核定位

#### 3.2 蛋白大小评估

**评价**: 293 aa，293 aa，适合生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 30 |
| 核定位分数 (weighted max) | 5 |
| Research hotness | 4.2676 |

**关键文献**:
1. Chen et al. (2021). "Upregulation of lncRNA NIFK-AS1 in hepatocellular carcinoma by m(6)A methylation promotes disease progression and sorafenib resistance.". *Hum Cell*. PMID: 34374933
2. Zhang et al. (2024). "Photoelectrocatalytic-Microbial Biohybrid for Nitrogen Reduction.". *Adv Mater*. PMID: 39233547
3. Xia et al. (2023). "The nucleolar protein NIFK accelerates the progression of colorectal cancer via activating MYC pathway.". *Biosci Biotechnol Biochem*. PMID: 37950567
4. Tan et al. (2023). "NIFK as a potential prognostic biomarker in colorectal cancer correlating with immune infiltrates.". *Medicine (Baltimore)*. PMID: 37800782
5. Lin et al. (2016). "The nucleolar protein NIFK promotes cancer progression via CK1α/β-catenin in metastasis and Ki-67-dependent cell proliferation.". *Elife*. PMID: 26984280
**评价**: PubMed 30篇，非常新颖

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 293 aa |
| PDB 条目数 | 25 |
| UniProt 注释结构域数 | 8 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/NIFK/NIFK-PAE.png]]

**评价**: 25 个 PDB 实验结构，实验验证充分

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | NIFK_FHA_Ki67-binding |
| InterPro | Nucleotide-bd_a/b_plait_sf |
| InterPro | RBD_domain_sf |
| InterPro | RRM_dom |
| Pfam | hNIFK_binding |
| Pfam | RRM_1 |
| SMART | RRM |
| PROSITE | RRM |

**染色质调控潜力分析**: 8 个结构域注释，新颖蛋白基线（存在新域发现潜力）

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

IntAct 实验互作: 0 条

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| RPF1 | 0 |  | 否 |
| RPF2 | 0 |  | 否 |
| BRIX1 | 0 |  | 否 |
| RSL1D1 | 0 |  | 否 |
| DDX18 | 0 |  | 否 |
| RRS1 | 0 |  | 否 |
| NIP7 | 0 |  | 否 |
| EBNA1BP2 | 0 |  | 否 |
| NOC2L | 0 |  | 否 |
| WDR12 | 0 |  | 否 |

**已知复合体成员** (GO Cellular Component):

- P:protein-containing complex assembly (GO:0065003, NAS:UniProtKB)

**PPI 互证分析**: STRING 15 partners，调控比例较低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 25 entries | 一致 |
| 结构域 | UniProt / InterPro / Pfam | 8 domains | 多库一致 |
| PPI | STRING + IntAct | 15 STRING + 0 IntAct | 单源 |
| 定位 | Protein Atlas / UniProt / GO | Nucleus | 多源一致 |

**互证加分明细**:
三维结构: AlphaFold + PDB 双源 (+0.5)
结构域: 多库注释一致 (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ★★★★☆ (4/5)

**核心优势**:
1. 新颖性: PubMed 30 篇，比较新颖
2. 核定位: 部分核定位

**风险/不确定性**:
1. HPA IF 数据可进一步验证
2. 25 PDB 结构可用

**下一步建议**:
- [ ] 验证核定位: IF 实验确认亚核定位
- [ ] 功能研究: 基于 PPI 网络设计功能实验
- [ ] 结构分析: 基于 PDB 结构设计功能实验

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=NIFK
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155438-NIFK
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22NIFK%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9BYG3
- STRING: https://string-db.org/network/9606.ENSG00000155438
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BYG3


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[NIFK-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/NIFK/NIFK-PAE.png]]


