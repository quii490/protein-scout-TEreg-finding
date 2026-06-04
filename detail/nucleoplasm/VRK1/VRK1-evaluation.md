---
type: protein-evaluation
gene: "VRK1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## VRK1 — REJECTED (研究热度过高 (PubMed strict=180，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VRK1 |
| 蛋白名称 | Serine/threonine-protein kinase VRK1 |
| 蛋白大小 | 396 aa / 45.5 kDa |
| UniProt ID | Q99986 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Nucleus, Cajal body |
| 蛋白大小 | 10/10 | ×1 | 10 | 396 aa / 45.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=180 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 2KTY, 2KUL, 2LAV, 2RSV, 3OP5, 5UKF, 5UVF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050235, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.0/180** | |
| **归一化总分** | | | **41.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Nucleus, Cajal body | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cajal body (GO:0015030)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi stack (GO:0005795)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 180 |
| PubMed broad count | 241 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Distal hereditary motor neuropathies.. *Revue neurologique*. PMID: 38702287
2. Histone Lactylation-Driven Upregulation of VRK1 Expression Promotes Stemness and Proliferation of Glioma Stem Cells.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40990975
3. VRK1 as a synthetic lethal target in VRK2 promoter-methylated cancers of the nervous system.. *JCI insight*. PMID: 36040810
4. EWS-FLI1 utilizes divergent chromatin remodeling mechanisms to directly activate or repress enhancer elements in Ewing sarcoma.. *Cancer cell*. PMID: 25453903
5. VRK1/BANF1/GLI1 Axis Regulates Tumor Development and Progression of Colorectal Cancer.. *International journal of biological sciences*. PMID: 40384864

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 2KTY, 2KUL, 2LAV, 2RSV, 3OP5, 5UKF, 5UVF, 6AC9, 6BP0, 6BRU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050235, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H2BC21 | 0.955 | 0.948 | — |
| ANKLE2 | 0.920 | 0.114 | — |
| BANF1 | 0.916 | 0.496 | — |
| H2BC8 | 0.916 | 0.916 | — |
| H2BC4 | 0.909 | 0.903 | — |
| H2AC17 | 0.903 | 0.900 | — |
| H2AC15 | 0.901 | 0.900 | — |
| H2AC13 | 0.901 | 0.900 | — |
| H2AC11 | 0.901 | 0.900 | — |
| H2AC16 | 0.901 | 0.900 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| COIL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21920476|imex:IM-15882 |
| ENSP00000506648.1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:21920476|imex:IM-15882 |
| TP53BP1 | psi-mi:"MI:0841"(phosphotransferase assay) | imex:IM-15883|pubmed:22621922 |
| JUN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15378002 |
| RAN | psi-mi:"MI:0096"(pull down) | imex:IM-9273|pubmed:18617507 |
| VRK3 | psi-mi:"MI:0096"(pull down) | imex:IM-9273|pubmed:18617507 |
| RCC1 | psi-mi:"MI:0096"(pull down) | imex:IM-9273|pubmed:18617507 |
| PLK3 | psi-mi:"MI:0096"(pull down) | imex:IM-9274|pubmed:19103756 |
| 22249" | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-9274|pubmed:19103756 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 2KTY, 2KUL, 2LAV, 2RSV, 3OP5,  | pLDDT=0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Nucleus, Cajal body / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. VRK1 — Serine/threonine-protein kinase VRK1，研究基础较多，新颖性有限。
2. 蛋白大小396 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 180 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 180 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99986
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100749-VRK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VRK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99986
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/VRK1/VRK1-PAE.png]]
