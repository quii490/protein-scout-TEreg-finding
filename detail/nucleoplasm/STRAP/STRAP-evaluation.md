---
type: protein-evaluation
gene: "STRAP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STRAP — REJECTED (研究热度过高 (PubMed strict=271，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STRAP / MAWD, UNRIP |
| 蛋白名称 | Serine-threonine kinase receptor-associated protein |
| 蛋白大小 | 350 aa / 38.4 kDa |
| UniProt ID | Q9Y3F4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Cell Junctions; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 350 aa / 38.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=271 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015943, IPR020472, IPR036322, IPR001680; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Cell Junctions | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- SMN complex (GO:0032797)
- SMN-Sm protein complex (GO:0034719)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 271 |
| PubMed broad count | 2481 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MAWD, UNRIP |

**关键文献**:
1. Predicting best treatment in rheumatoid arthritis.. *Seminars in arthritis and rheumatism*. PMID: 38008706
2. A novel mitochondrial quality regulation gene signature for anticipating prognosis, TME, and therapeutic response in LUAD by multi-omics analysis and experimental verification.. *Cancer cell international*. PMID: 40211263
3. FTO downregulation mediated by hypoxia facilitates colorectal cancer metastasis.. *Oncogene*. PMID: 34218271
4. Single-cell image-based screens identify host regulators of Ebola virus infection dynamics.. *Nature microbiology*. PMID: 40707832
5. CircPCNXL2 promotes tumor growth and metastasis by interacting with STRAP to regulate ERK signaling in intrahepatic cholangiocarcinoma.. *Molecular cancer*. PMID: 38365721

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.6 |
| 高置信度残基 (pLDDT>90) 占比 | 84.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.9% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 11.4% |
| 有序区域 (pLDDT>70) 占比 | 86.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.6，有序区 86.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR020472, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GEMIN7 | 0.999 | 0.865 | — |
| GEMIN6 | 0.999 | 0.838 | — |
| GEMIN2 | 0.999 | 0.782 | — |
| SMN1 | 0.998 | 0.878 | — |
| DDX20 | 0.997 | 0.836 | — |
| GEMIN8 | 0.996 | 0.790 | — |
| GEMIN5 | 0.995 | 0.644 | — |
| GEMIN4 | 0.990 | 0.768 | — |
| SMN2 | 0.990 | 0.000 | — |
| PBLD | 0.984 | 0.234 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000392270.2 | psi-mi:"MI:0096"(pull down) | pubmed:17314099|imex:IM-19294 |
| MTRES1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TNIK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSK3B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RNPS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GH1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NME2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.6 + PDB: 无 | pLDDT=89.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. STRAP — Serine-threonine kinase receptor-associated protein，研究基础较多，新颖性有限。
2. 蛋白大小350 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 271 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 271 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3F4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000023734-STRAP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STRAP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3F4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
