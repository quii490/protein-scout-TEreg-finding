---
type: protein-evaluation
gene: "TBP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TBP — REJECTED (研究热度过高 (PubMed strict=3124，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBP / GTF2D1, TF2D, TFIID |
| 蛋白名称 | TATA-box-binding protein |
| 蛋白大小 | 339 aa / 37.7 kDa |
| UniProt ID | P20226 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 339 aa / 37.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3124 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.1; PDB: 1C9B, 1CDW, 1JFI, 1NVP, 1TGH, 4ROC, 4ROD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000814, IPR030491, IPR012295, IPR033710; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- euchromatin (GO:0000791)
- female germ cell nucleus (GO:0001674)
- female pronucleus (GO:0001939)
- male germ cell nucleus (GO:0001673)
- male pronucleus (GO:0001940)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3124 |
| PubMed broad count | 5568 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GTF2D1, TF2D, TFIID |

**关键文献**:
1. The roles of TAF1 in neuroscience and beyond.. *Royal Society open science*. PMID: 39323550
2. Spinocerebellar Ataxia Type 17 (SCA17).. *Advances in experimental medicine and biology*. PMID: 29427105
3. Structures and implications of TBP-nucleosome complexes.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 34301908
4. Role of the TATA-box binding protein (TBP) and associated family members in transcription regulation.. *Gene*. PMID: 35597524
5. LncRNA-TBP mediates TATA-binding protein recruitment to regulate myogenesis and induce slow-twitch myofibers.. *Cell communication and signaling : CCS*. PMID: 36635672

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.1 |
| 高置信度残基 (pLDDT>90) 占比 | 51.6% |
| 置信残基 (pLDDT 70-90) 占比 | 13.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 23.9% |
| 有序区域 (pLDDT>70) 占比 | 64.6% |
| 可用 PDB 条目 | 1C9B, 1CDW, 1JFI, 1NVP, 1TGH, 4ROC, 4ROD, 4ROE, 5FUR, 5IY6 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1C9B, 1CDW, 1JFI, 1NVP, 1TGH, 4ROC, 4ROD, 4ROE, 5FUR, 5IY6）+ AlphaFold极高置信度预测（pLDDT=77.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000814, IPR030491, IPR012295, IPR033710; Pfam: PF00352 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POLR2A | 0.999 | 0.990 | — |
| TAF9 | 0.999 | 0.999 | — |
| TAF8 | 0.999 | 0.993 | — |
| TAF6 | 0.999 | 0.999 | — |
| BRF2 | 0.999 | 0.970 | — |
| GTF2A1 | 0.999 | 0.997 | — |
| TAF3 | 0.999 | 0.998 | — |
| TAF7 | 0.999 | 0.999 | — |
| GTF2E1 | 0.999 | 0.971 | — |
| BRF1 | 0.999 | 0.971 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TAF1L | psi-mi:"MI:0018"(two hybrid) | pubmed:12217962 |
| GTF2A1 | psi-mi:"MI:0401"(biochemical) | pubmed:8006019 |
| GTF2B | psi-mi:"MI:0401"(biochemical) | pubmed:8006019 |
| HMGB1 | psi-mi:"MI:0401"(biochemical) | pubmed:8006019 |
| MDM2 | psi-mi:"MI:0096"(pull down) | pubmed:9271120 |
| NFKBIB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| mrt-2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:14704431|imex:IM-16523| |
| mdf-2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:14704431|imex:IM-16523| |
| TP53 | psi-mi:"MI:0047"(far western blotting) | pubmed:7799929 |
| Arp10 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.1 + PDB: 1C9B, 1CDW, 1JFI, 1NVP, 1TGH,  | pLDDT=77.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. TBP — TATA-box-binding protein，研究基础较多，新颖性有限。
2. 蛋白大小339 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3124 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3124 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P20226
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112592-TBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P20226
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
