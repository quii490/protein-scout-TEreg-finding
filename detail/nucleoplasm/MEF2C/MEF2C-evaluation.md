---
type: protein-evaluation
gene: "MEF2C"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MEF2C — REJECTED (研究热度过高 (PubMed strict=1281，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEF2C |
| 蛋白名称 | Myocyte-specific enhancer factor 2C |
| 蛋白大小 | 473 aa / 51.2 kDa |
| UniProt ID | Q06413 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; UniProt: Nucleus; Cytoplasm, sarcoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 473 aa / 51.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1281 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR022102, IPR033896, IPR002100, IPR036879; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Supported |
| UniProt | Nucleus; Cytoplasm, sarcoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- postsynapse (GO:0098794)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1281 |
| PubMed broad count | 1879 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. MEF2C promotes M1 macrophage polarization and Th1 responses.. *Cellular & molecular immunology*. PMID: 35194174
2. MEF2C regulates NK cell effector functions through control of lipid metabolism.. *Nature immunology*. PMID: 38589619
3. The transcription factor MEF2C restrains microglial overactivation by inhibiting kinase CDK2.. *Immunity*. PMID: 40139186
4. Mutations in the spliceosomal gene SNW1 cause neurodevelopment disorders with microcephaly.. *The Journal of clinical investigation*. PMID: 40608414
5. Whole-brain in vivo base editing reverses behavioral changes in Mef2c-mutant mice.. *Nature neuroscience*. PMID: 38012399

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.7 |
| 高置信度残基 (pLDDT>90) 占比 | 18.6% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.5% |
| 低置信 (pLDDT<50) 占比 | 64.5% |
| 有序区域 (pLDDT>70) 占比 | 22.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.7），有序残基占 22.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022102, IPR033896, IPR002100, IPR036879; Pfam: PF12347, PF00319 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NKX2-5 | 0.988 | 0.617 | — |
| HDAC4 | 0.984 | 0.865 | — |
| GATA4 | 0.969 | 0.071 | — |
| MYOG | 0.964 | 0.299 | — |
| MYOD1 | 0.956 | 0.476 | — |
| MAPK7 | 0.956 | 0.564 | — |
| PPARGC1A | 0.943 | 0.045 | — |
| MEF2A | 0.940 | 0.628 | — |
| CTNNB1 | 0.939 | 0.000 | — |
| HDAC5 | 0.924 | 0.466 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Acly | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| PLA2G12A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MAPK14 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| COPS5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| EPAS1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| HDAC9 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| MAPK7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| SPTBN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| YWHAZ | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| TFCP2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.7 + PDB: 无 | pLDDT=55.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, sarcoplasm / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MEF2C — Myocyte-specific enhancer factor 2C，研究基础较多，新颖性有限。
2. 蛋白大小473 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1281 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1281 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q06413
- Protein Atlas: https://www.proteinatlas.org/ENSG00000081189-MEF2C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEF2C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q06413
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
