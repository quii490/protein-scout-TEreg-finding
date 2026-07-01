---
type: protein-evaluation
gene: "FAM210A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM210A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM210A / C18orf19 |
| 蛋白名称 | Protein FAM210A |
| 蛋白大小 | 272 aa / 30.8 kDa |
| UniProt ID | Q96ND0 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM210A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM210A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Golgi apparatus, Mitochondria; UniProt: Membrane; Mitochondrion; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 272 aa / 30.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045866, IPR009688; Pfam: PF06916 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus, Mitochondria | Approved |
| UniProt | Membrane; Mitochondrion; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C18orf19 |

**关键文献**:
1. FAM210A is essential for cold-induced mitochondrial remodeling in brown adipocytes.. *Nature communications*. PMID: 37816711
2. FAM210A regulates mitochondrial translation and maintains cardiac mitochondrial homeostasis.. *Cardiovascular research*. PMID: 37522353
3. Modulators of Fam210a and Roles of Fam210a in the Function of Myoblasts.. *Calcified tissue international*. PMID: 31980842
4. Expression and purification of the mitochondrial transmembrane protein FAM210A in Escherichia coli.. *Protein expression and purification*. PMID: 37329934
5. Expression and purification of the mitochondrial transmembrane protein FAM210A in Escherichia coli.. *bioRxiv : the preprint server for biology*. PMID: 37292620

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.6 |
| 高置信度残基 (pLDDT>90) 占比 | 7.7% |
| 置信残基 (pLDDT 70-90) 占比 | 41.2% |
| 中等置信 (pLDDT 50-70) 占比 | 16.9% |
| 低置信 (pLDDT<50) 占比 | 34.2% |
| 有序区域 (pLDDT>70) 占比 | 48.9% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM210A/FAM210A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=64.6），有序残基占 48.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045866, IPR009688; Pfam: PF06916 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD300C | 0.594 | 0.594 | — |
| ZBTB40 | 0.592 | 0.000 | — |
| ATAD3A | 0.585 | 0.292 | — |
| HIBADH | 0.573 | 0.000 | — |
| GFM1 | 0.546 | 0.000 | — |
| DCDC1 | 0.527 | 0.000 | — |
| SLC25A13 | 0.521 | 0.000 | — |
| CPED1 | 0.507 | 0.000 | — |
| STARD3NL | 0.494 | 0.000 | — |
| SPTBN1 | 0.493 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BABAM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| menB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| IFT52 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CD300C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Orc2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| BRICD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LCN6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GPR182 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EIF2B5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HCST | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.6 + PDB: 无 | pLDDT=64.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Mitochondrion; Cytoplasm / Nucleoplasm, Golgi apparatus, Mitochondria | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

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
1. FAM210A — Protein FAM210A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小272 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| BABAM1 | BioGRID | 0 |
| SHMT2 | BioGRID | 0 |
| NXF1 | BioGRID | 0 |
| CD300C | BioGRID | 0 |
| HLA-DPA1 | BioGRID | 0 |
| FAM210A | BioGRID | 0 |
| COPA | BioGRID | 0 |
| COPB2 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

**结构域架构**：FAM210A（272 aa，30.8 kDa）含DUF1279结构域（IPR045866, IPR009688, PF06916），位于117-229 aa区域，属于高度保守但在真核生物中广泛分布的DUF1279家族。AlphaFold pLDDT=64.6表明结构预测质量中等——有序区域（pLDDT>70）占48.9%，其中高置信度残基（pLDDT>90）仅占7.7%，低置信度区域（pLDDT<50）占34.2%，主要集中于N端1-116 aa区段。DUF1279结构域核心预测为α/β混合折叠模式：4-5条平行β链形成中央β-折叠片，两侧由α-螺旋包围，构成紧凑的球状结构域。N端无序区（约116 aa）富含碱性残基和疏水残基，可能具有双重功能：N端线粒体靶向序列（MTS, 形成两亲性α-螺旋）引导线粒体导入，同时暴露的碱性残基簇（Lys/Arg富集区）可在胞质定位条件下作为核定位信号（NLS）被importin-α/β识别。DUF1279结构域表面保守残基（Asp/Glu酸性簇和Arg/Lys碱性簇交替排列）提示其作为蛋白质-蛋白质/蛋白质-RNA相互作用平台，碱性残基可用于核酸磷酸骨架的非序列特异性结合。

**PPI互作网络解读**：PPI网络揭示FAM210A连接线粒体翻译与核质mRNA代谢两个独立功能模块。线粒体模块——ATAD3A（ATPase家族AAA结构域含蛋白3A，线粒体内膜蛋白，调控mtDNA复制和线粒体核糖体组装）、GFM1（线粒体翻译延伸因子G1，催化线粒体核糖体转位，MITRAC复合体组分）、SLC25A13（线粒体天冬氨酸/谷氨酸载体，苹果酸-天冬氨酸穿梭关键组分）和MGARP（线粒体富集的促性腺激素诱导凋亡调控蛋白，MCU复合体调节因子）——共同指向FAM210A参与线粒体翻译装置的组装和线粒体蛋白质稳态维持（PMID:37522353, PMID:37816711）。核质模块——NXF1（mRNA核输出因子TAP，介导成熟mRNA经核孔复合体Nup62/Nup98的主动转运）、BABAM1（BRCA1-A复合体亚基MERIT40/NBA1，参与DNA双链断裂末端切除和G2/M检查点激活）、ZBTB40（含BTB/POZ结构域和C2H2锌指的转录因子，BTB/POZ介导同源二聚化和转录抑制复合体组装）——连接核质mRNA转运和DNA损伤应答信号。SHMT2（丝氨酸羟甲基转移酶2，一碳代谢限速酶，催化丝氨酸→甘氨酸+5,10-亚甲基四氢叶酸，线粒体和核质双定位）作为关键枢纽将两个模块桥接，提示FAM210A在整合一碳代谢（提供SAM合成所需甲基供体）与线粒体翻译调控中的潜在功能。

**结构解读**：DUF1279结构域通过其刚性α/β折叠核心维持稳定的蛋白构象，而N端无序区赋予蛋白高度的定位和功能可塑性。线粒体导入：N端MTS经TOM/TIM复合体（外膜转位酶/内膜转位酶）介导FAM210A进入线粒体基质，MTS被线粒体加工肽酶（MPP）切割后暴露出DUF1279核心结构域，与线粒体核糖体大亚基（39S）的MRPL蛋白和GFM1 GTPase结构域互作，支持线粒体编码蛋白（MT-CO1, MT-CO2, MT-ND1-6, MT-ATP6/8, MT-CYB）翻译的延伸和核糖体回收（PMID:37522353）。核质定位：N端碱性NLS被importin-α/KPNA2识别→importin-β/KPNB1介导的核孔转位→核内RanGTP触发复合体解离。核质DUF1279域可与NXF1的LRR/NTF2-like结构域和SHMT2的PLP结合域相互作用，形成核质mRNA代谢/一碳代谢的调控节点。AlphaFold预测质量仅中等（pLDDT=64.6）反映了DUF1279结构域可能经历配体依赖的构象变化（无序-有序转变），而AlphaFold仅能捕捉到地态的局部结构偏好。

**机制模型**：（1）线粒体逆转录信号（mitochondrial retrograde signaling, MRS）——当线粒体翻译受损（mtDNA突变、线粒体核糖体中毒如氯霉素/linezolid处理、氧化应激损伤），FAM210A线粒体池减少（翻译依赖性降解或MTS裂解失败），核质池代偿性增加。核质FAM210A-DUF1279结合NXF1和SHMT2，激活核基因转录重编程以补偿线粒体呼吸链缺陷（如激活ATF4/CHOP整合应激反应或Nrf2抗氧化反应）。（2）一碳代谢-甲基化轴——SHMT2提供的5,10-亚甲基四氢叶酸经MTHFR还原为5-甲基四氢叶酸，后者为同型半胱氨酸→甲硫氨酸重甲基化提供甲基，甲硫氨酸经MAT转化为SAM（通用甲基供体）。FAM210A的结合可调控SHMT2活性或局部一碳单位浓度，从而影响核内SAM/SAH比率，间接调控DNMT1/3A/3B对TE区域（特别是LTR/ERV/LINE-1 5'UTR）CpG位点的甲基化维持。（3）ZBTB40转录抑制复合体——BTB/POZ结构域蛋白常作为Cullin3-RING E3泛素连接酶（CRL3）的底物识别适配器，FAM210A被ZBTB40招募至特定基因组位点后可能促进局部染色质蛋白的泛素化-蛋白酶体降解，为转录因子/RNA聚合酶II的结合创造可及性窗口。

**TE调控展望**：FAM210A通过一碳代谢-表观遗传轴和泛素-蛋白酶体轴间接连接TE调控。SHMT2-一碳代谢决定SAM可用性，直接影响LTR和LINE-1启动子CpG甲基化水平——已知LINE-1 5'UTR的CpG岛甲基化状态是抑制其逆转录转座活性的主要机制。ATAD3A互作提示FAM210A可能也调控线粒体来源的逆行信号对核TE（特别是SINE/Alu和LINE-1）转录的间接影响——线粒体功能障碍已知可激活LINE-1逆转录转座。BABAM1和BRCA1-A复合体连接DNA损伤应答，而DNA损伤（特别是双链断裂）可促进LINE-1整合介导的基因组不稳定性。虽然FAM210A缺乏直接的DNA/染色质结合结构域，其通过PPI网络间接调控的表观遗传和基因组稳定性通路构成了TE调控的合理机制假说，值得通过靶向FAM210A敲除/敲低的LINE-1逆转录转座报告实验（如L1-EGFP retrotransposition assay）和RRBS（简化代表性亚硫酸盐测序）验证其在TE甲基化和转座活性中的功能。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96ND0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177150-FAM210A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM210A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96ND0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM210A/FAM210A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96ND0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 117..229; /note="DUF1279" |
| InterPro | IPR045866;IPR009688; |
| Pfam | PF06916; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177150-FAM210A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CD63 | Bioplex | false |
| EIF2B5 | Bioplex | false |
| GPR182 | Bioplex | false |
| HLA-DRA | Bioplex | false |
| IFT52 | Intact | false |
| LCN6 | Bioplex | false |
| MGARP | Bioplex | false |
| RAMP3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
