---
type: protein-evaluation
gene: "Anp32a"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Anp32a — REJECTED (研究热度过高 (PubMed strict=105，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Anp32a / C15orf1, LANP, MAPM, PHAP1 |
| 蛋白名称 | Acidic leucine-rich nuclear phosphoprotein 32 family member A |
| 蛋白大小 | 249 aa / 28.6 kDa |
| UniProt ID | P39687 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centrosome, Cytosol; UniProt: Nucleus; Cytoplasm; Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 249 aa / 28.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=105 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.9; PDB: 2JE0, 2JE1, 4XOS, 6XZQ, 8RMR, 8RN0, 8RNA |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045081, IPR001611, IPR032675, IPR003603; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 105 |
| PubMed broad count | 205 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf1, LANP, MAPM, PHAP1 |

**关键文献**:
1. Creating resistance to avian influenza infection through genome editing of the ANP32 gene family.. *Nature communications*. PMID: 37816720
2. Species difference in ANP32A underlies influenza A virus polymerase host restriction.. *Nature*. PMID: 26738596
3. Human ANP32A/B are SUMOylated and utilized by avian influenza virus NS2 protein to overcome species-specific restriction.. *Nature communications*. PMID: 39737943
4. ANP32A promotes the proliferation, migration and invasion of hepatocellular carcinoma by modulating the HMGA1/STAT3 pathway.. *Carcinogenesis*. PMID: 33332531
5. Hypoxia and Wnt signaling inversely regulate expression of chondroprotective molecule ANP32A in articular cartilage.. *Osteoarthritis and cartilage*. PMID: 36370958

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.9 |
| 高置信度残基 (pLDDT>90) 占比 | 61.8% |
| 置信残基 (pLDDT 70-90) 占比 | 1.2% |
| 中等置信 (pLDDT 50-70) 占比 | 25.7% |
| 低置信 (pLDDT<50) 占比 | 11.2% |
| 有序区域 (pLDDT>70) 占比 | 63.0% |
| 可用 PDB 条目 | 2JE0, 2JE1, 4XOS, 6XZQ, 8RMR, 8RN0, 8RNA, 8RNB, 8RNC |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2JE0, 2JE1, 4XOS, 6XZQ, 8RMR, 8RN0, 8RNA, 8RNB, 8RNC）+ AlphaFold极高置信度预测（pLDDT=79.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045081, IPR001611, IPR032675, IPR003603; Pfam: PF14580 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SET | 0.999 | 0.628 | — |
| APEX1 | 0.996 | 0.292 | — |
| NME1 | 0.978 | 0.000 | — |
| XPO1 | 0.974 | 0.292 | — |
| ELAVL1 | 0.971 | 0.292 | — |
| PTMA | 0.872 | 0.000 | — |
| PPP2CA | 0.851 | 0.292 | — |
| NUP214 | 0.847 | 0.000 | — |
| GZMA | 0.841 | 0.000 | — |
| ATXN1 | 0.818 | 0.239 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Nfatc2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| TRAF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| AXIN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NSFL1C | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HSPB3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| KPNA1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| KPNA5 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| KPNA6 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| PCBP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19805454|imex:IM-19495 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.9 + PDB: 2JE0, 2JE1, 4XOS, 6XZQ, 8RMR,  | pLDDT=79.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Endoplasmic reticulum / Nucleoplasm; 额外: Centrosome, Cytosol | 一致 |
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
1. Anp32a — Acidic leucine-rich nuclear phosphoprotein 32 family member A，研究基础较多，新颖性有限。
2. 蛋白大小249 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 105 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 105 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P39687
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140350-ANP32A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Anp32a
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P39687
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
