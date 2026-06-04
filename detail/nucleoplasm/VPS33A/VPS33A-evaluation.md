---
type: protein-evaluation
gene: "VPS33A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VPS33A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VPS33A |
| 蛋白名称 | Vacuolar protein sorting-associated protein 33A |
| 蛋白大小 | 596 aa / 67.6 kDa |
| UniProt ID | Q96AX1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasmic vesicle; Late endosome membrane; Lysosome membra |
| 蛋白大小 | 10/10 | ×1 | 10 | 596 aa / 67.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=52 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=93.9; PDB: 4BX8, 4BX9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR043154, IPR043127, IPR001619, IPR027482, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasmic vesicle; Late endosome membrane; Lysosome membrane; Early endosome; Cytoplasmic vesicle,... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- autophagosome (GO:0005776)
- clathrin-coated vesicle (GO:0030136)
- CORVET complex (GO:0033263)
- early endosome (GO:0005769)
- endosome membrane (GO:0010008)
- HOPS complex (GO:0030897)
- late endosome (GO:0005770)
- late endosome membrane (GO:0031902)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 52 |
| PubMed broad count | 60 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mucopolysaccharidosis-Plus Syndrome.. *International journal of molecular sciences*. PMID: 31936524
2. The hookup model of the HOPS complex in autophagosome-lysosome fusion.. *Autophagy*. PMID: 38083843
3. Proteomic and Biochemical Comparison of the Cellular Interaction Partners of Human VPS33A and VPS33B.. *Journal of molecular biology*. PMID: 29778605
4. The lysosomal disease caused by mutant VPS33A.. *Human molecular genetics*. PMID: 31070736
5. The use of genistein and ambroxol may be an effective approach in correcting cellular dysfunctions of mucopolysaccharidosis-plus syndrome.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 41310305

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.9 |
| 高置信度残基 (pLDDT>90) 占比 | 86.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 96.3% |
| 可用 PDB 条目 | 4BX8, 4BX9 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4BX8, 4BX9）+ AlphaFold高质量预测（pLDDT=93.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043154, IPR043127, IPR001619, IPR027482, IPR036045; Pfam: PF00995 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS16 | 0.999 | 0.999 | — |
| VPS41 | 0.999 | 0.981 | — |
| VPS11 | 0.999 | 0.977 | — |
| VPS39 | 0.999 | 0.998 | — |
| VPS18 | 0.999 | 0.981 | — |
| TGFBRAP1 | 0.996 | 0.963 | — |
| VPS8 | 0.991 | 0.914 | — |
| VIPAS39 | 0.978 | 0.369 | — |
| STX7 | 0.961 | 0.769 | — |
| STX12 | 0.951 | 0.748 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| ENSP00000267199.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| UVRAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| VIPAS39 | psi-mi:"MI:0663"(confocal microscopy) | pubmed:19109425|imex:IM-20415 |
| MON1B | psi-mi:"MI:0096"(pull down) | imex:IM-14140|pubmed:20434987 |
| MON1A | psi-mi:"MI:0096"(pull down) | imex:IM-14140|pubmed:20434987 |
| VPS16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20190753|imex:IM-19065 |
| VPS41 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAB5A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.9 + PDB: 4BX8, 4BX9 | pLDDT=93.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle; Late endosome membrane; Lysos / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. VPS33A — Vacuolar protein sorting-associated protein 33A，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小596 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 52 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AX1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139719-VPS33A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VPS33A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AX1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
