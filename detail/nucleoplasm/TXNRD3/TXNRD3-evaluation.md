---
type: protein-evaluation
gene: "TXNRD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TXNRD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TXNRD3 / TGR, TRXR3, TXNRD3IT1, TXNRD3NB |
| 蛋白名称 | Thioredoxin reductase 3 |
| 蛋白大小 | 643 aa / 70.7 kDa |
| UniProt ID | Q86VQ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus; Microsome; Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 643 aa / 70.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 3H8Q |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036188, IPR023753, IPR016156, IPR002109, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus; Microsome; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 108 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TGR, TRXR3, TXNRD3IT1, TXNRD3NB |

**关键文献**:
1. Selenoprotein Gene Nomenclature.. *The Journal of biological chemistry*. PMID: 27645994
2. Selenoprotein TXNRD3 supports male fertility via the redox regulation of spermatogenesis.. *The Journal of biological chemistry*. PMID: 35753352
3. [Effect of Selenoprotein Thioredoxin Reductase 3 on the Survival Prognosis of Tumor Patients].. *Zhongguo yi xue ke xue yuan xue bao. Acta Academiae Medicinae Sinicae*. PMID: 36621786
4. Role of Txnrd3 in NiCl(2)-induced kidney cell apoptosis in mice: Potential therapeutic effect of melatonin.. *Ecotoxicology and environmental safety*. PMID: 37757623
5. [Epidermal factor Foxn1 as a regulator of antioxidant defense in the skin].. *Postepy biochemii*. PMID: 39012697

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 3H8Q |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036188, IPR023753, IPR016156, IPR002109, IPR011899; Pfam: PF00462, PF07992, PF02852 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SEPHS2 | 0.979 | 0.000 | — |
| SCLY | 0.943 | 0.000 | — |
| TXN | 0.942 | 0.186 | — |
| SEPHS1 | 0.942 | 0.000 | — |
| CTH | 0.928 | 0.000 | — |
| KYAT3 | 0.918 | 0.046 | — |
| KYAT1 | 0.918 | 0.046 | — |
| TXNRD2 | 0.907 | 0.000 | — |
| TXNRD1 | 0.904 | 0.000 | — |
| GPX2 | 0.857 | 0.063 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H2AC12 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ANKRD36B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SNAP29 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PACRGL | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CTNNA3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CINP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BOLA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BOLA2-SMG1P6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FHL2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ATE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 3H8Q | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Microsome; Endoplasmic reticul / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TXNRD3 — Thioredoxin reductase 3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小643 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86VQ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197763-TXNRD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TXNRD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86VQ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
