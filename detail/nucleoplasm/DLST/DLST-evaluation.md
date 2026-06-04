---
type: protein-evaluation
gene: "DLST"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DLST — REJECTED (研究热度过高 (PubMed strict=137，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLST / DLTS |
| 蛋白名称 | Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex, mitochondrial |
| 蛋白大小 | 453 aa / 48.8 kDa |
| UniProt ID | P36957 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitochondria, Cytosol; UniProt: Mitochondrion matrix; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 453 aa / 48.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=137 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.4; PDB: 6H05 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003016, IPR050537, IPR001078, IPR000089, IPR023 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitochondria, Cytosol | Supported |
| UniProt | Mitochondrion matrix; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- membrane (GO:0016020)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- oxoadipate dehydrogenase complex (GO:0160167)
- oxoglutarate dehydrogenase complex (GO:0045252)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 137 |
| PubMed broad count | 400 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DLTS |

**关键文献**:
1. ATF3/SPI1/SLC31A1 Signaling Promotes Cuproptosis Induced by Advanced Glycosylation End Products in Diabetic Myocardial Injury.. *International journal of molecular sciences*. PMID: 36675183
2. 4-Octyl itaconate inhibits aerobic glycolysis by targeting GAPDH to promote cuproptosis in colorectal cancer.. *Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*. PMID: 36706634
3. Succinate drives gut inflammation by promoting FOXP3 degradation through a molecular switch.. *Nature immunology*. PMID: 40457062
4. Identification of hub cuproptosis related genes and immune cell infiltration characteristics in periodontitis.. *Frontiers in immunology*. PMID: 37215133
5. Defective function of α-ketoglutarate dehydrogenase exacerbates mitochondrial ATP deficits during complex I deficiency.. *Redox biology*. PMID: 37883842

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.4 |
| 高置信度残基 (pLDDT>90) 占比 | 42.8% |
| 置信残基 (pLDDT 70-90) 占比 | 25.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 22.7% |
| 有序区域 (pLDDT>70) 占比 | 68.2% |
| 可用 PDB 条目 | 6H05 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=76.4，有序区 68.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003016, IPR050537, IPR001078, IPR000089, IPR023213; Pfam: PF00198, PF00364 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DHTKD1 | 0.999 | 0.466 | — |
| OGDH | 0.999 | 0.953 | — |
| OGDHL | 0.999 | 0.935 | — |
| DLD | 0.999 | 0.906 | — |
| SUCLG1 | 0.995 | 0.099 | — |
| SUCLA2 | 0.989 | 0.242 | — |
| SUCLG2 | 0.981 | 0.099 | — |
| PDHB | 0.974 | 0.530 | — |
| BCKDHB | 0.968 | 0.516 | — |
| BCKDHA | 0.963 | 0.312 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| TBPH | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ZHX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ZBTB16 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TUBB2A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ARIH2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PAK4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| DLG5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PFN2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FLII | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.4 + PDB: 6H05 | pLDDT=76.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion matrix; Nucleus / Nucleoplasm; 额外: Mitochondria, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DLST — Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小453 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 137 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 137 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P36957
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119689-DLST/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLST
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P36957
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
