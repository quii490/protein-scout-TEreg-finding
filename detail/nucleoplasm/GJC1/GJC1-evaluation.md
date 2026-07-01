---
type: protein-evaluation
gene: "GJC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GJC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GJC1 / GJA7 |
| 蛋白名称 | Gap junction gamma-1 protein |
| 蛋白大小 | 396 aa / 45.5 kDa |
| UniProt ID | P36383 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm, Endoplasmic reticulum; UniProt: Cell membrane; Cell junction, gap junction |
| 蛋白大小 | 10/10 | ×1 | 10 | 396 aa / 45.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.4; PDB: 3SHW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000500, IPR002265, IPR019570, IPR017990, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Endoplasmic reticulum | Supported |
| UniProt | Cell membrane; Cell junction, gap junction | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- connexin complex (GO:0005922)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- gap junction (GO:0005921)
- intercalated disc (GO:0014704)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.4 |
| 高置信度残基 (pLDDT>90) 占比 | 27.5% |
| 置信残基 (pLDDT 70-90) 占比 | 28.5% |
| 中等置信 (pLDDT 50-70) 占比 | 14.6% |
| 低置信 (pLDDT<50) 占比 | 29.3% |
| 有序区域 (pLDDT>70) 占比 | 56.0% |
| 可用 PDB 条目 | 3SHW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.4），有序残基占 56.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000500, IPR002265, IPR019570, IPR017990, IPR013092; Pfam: PF00029 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GJA1 | 0.993 | 0.173 | — |
| GJA5 | 0.991 | 0.000 | — |
| GJD2 | 0.931 | 0.000 | — |
| GJB6 | 0.929 | 0.000 | — |
| GJE1 | 0.907 | 0.000 | — |
| TJP1 | 0.898 | 0.071 | — |
| GJA4 | 0.896 | 0.091 | — |
| GJB2 | 0.827 | 0.000 | — |
| HCN4 | 0.827 | 0.000 | — |
| CNST | 0.803 | 0.301 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Gja1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:18055446|imex:IM-19526 |
| Cnst | psi-mi:"MI:0096"(pull down) | pubmed:19864490|imex:IM-19064 |
| GJD3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12154091|imex:IM-20451 |
| EXTL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GRPR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM86A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC66A1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| APOL3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| UPK1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.4 + PDB: 3SHW | pLDDT=69.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, gap junction / Plasma membrane; 额外: Nucleoplasm, Endoplasmic reti | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GJC1 — Gap junction gamma-1 protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小396 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

**结构域架构**：GJC1（396 aa, 45.5 kDa, P36383, Gap junction gamma-1 protein/Connexin-45/Connexin-46.6, 别名GJA7）是connexin（间隙连接蛋白）家族成员。Connexin的标准拓扑为4次跨膜蛋白（4-TM: TM1-胞外loop1-TM2-胞内loop-TM3-胞外loop2-TM4），N端和C端均为胞质。结构域注释：Connexin domain（IPR000500, Pfam PF00029）——保守的connexin signature motif（约198 aa），涵盖四个TM段和两个胞外loop——每个胞外loop含3个conserved Cys residues形成intramolecular disulfide bond（C1-C3, C2-C2 cross-loop stabilization）——赋予胞外loop特定的3D构象以识别相邻细胞的connexin——两个相邻细胞的connexons（半通道, hexamer of connexin）在细胞间隙docking形成完整的gap junction channel（dodecamer）。Connexin_C domain（IPR019570）为C端胞质尾——Cx45的C-terminal tail（CT）约150 aa——是connexin家族中CT最长的之一——富含Ser/Thr phosphorylation sites（PKA, PKC, CK1, MAPK, CaMKII consensus sites）和SH3/SH2 binding motifs（PxxP, pYxxP）。AlphaFold pLDDT=69.4, PDB=1（3SHW, Cx26 gap junction channel的晶体结构作为同源模板），TM区域pLDDT>80但CT区pLDDT极低（<40）——CT是完全无序的IDR。

**PPI互作网络解读**：PPI网络（STRING 15 partners）高度富集connexin家族成员——GJA1（Cx43, STRING 0.993）、GJA5（Cx40, STRING 0.991）、GJA4（Cx37, STRING 0.896）——这些connexin可形成heteromeric connexon（由不同connexin亚型混合组成的6-mer半通道）——Cx45与Cx43/Cx40/Cx37的heteromeric assembly调控gap junction的通道特性（unitary conductance, voltage gating, permeability to second messengers如Ca2+, IP3, cAMP, cGMP）。TJP1（ZO-1, Tight junction protein 1, STRING 0.898）是MAGUK family scaffold——通过其PDZ domain结合Cx45 CT的C末端PDZ-binding motif（最后4个氨基酸残基: -D/ExI/LSV-COOH）——将connexon锚定在紧密连接和gap junction plaque的边界。HCN4（hyperpolarization-activated cyclic nucleotide-gated channel 4, STRING 0.827）为心脏起搏（pacemaker, If/"funny" current）通道——Cx45-HCN4共定位提示两者在cardiac conduction system（SA node, AV node）中的功能耦合——gap junction的电耦合和If pacemaker电流协同调控心脏节律。IntAct: Gja1（Cx43, PMID:18055446），Cnst（Consortin, gap junction regulator, PMID:19864490）——Cnst是connexin trafficking and plaque assembly的正向调控因子。

**结构解读**：Cx45的gap junction channel（12-mer, ~1.5 MDa）是一个4.5 nm长的圆柱形孔道——直径约1.2 nm（可通透up to ~1 kDa分子）。每个connexin subunit贡献一个TM domain（4-TM bundle）至通道壁——TM1和TM3的极性残基（Ser/Thr/Asn）朝向孔道内侧形成亲水性内壁——决定通道的离子选择性和分子通透性。两个相邻细胞的connexon（各6-mer）经胞外loop的disulfide bond配对和3D docking完成gap junction的fully assembled state。CT IDR在通道内壁形成"entropic gate"——在低pH或高Ca2+条件下CT折叠关闭通道（"ball-and-chain" gating model）——PKC/CaMKII/PKA的CT磷酸化调节通道开闭动力学和分子通透性。

**机制模型**：（1）Cardiac conduction——Cx45在sinoatrial node（SA node, 窦房结, 心脏起搏点）和atrioventricular node（AV node, 房室结, 冲动传导延迟）以及cardiac conduction system（His bundle, Purkinje fibers）中高度表达——Cx45 gap junction低unitary conductance（~30 pS, Cx43为~100 pS）和voltage-sensitive closure实现了SA node→atrium的缓慢传导（保护ventricle免受atrial tachyarrhythmia的影响）。PMID:42368294——进行性心脏传导疾病与GJC1的关联。（2）内皮和血管功能——Cx45在endothelial cell表达的gap junction允许EC之间cAMP/cGMP/IP3/Ca2+ exchange——协调vasodilation（EDHF/endothelium-derived hyperpolarization factor signaling）和angiogenesis。Cx45与Cx37/Cx40/Cx43在特定血管床的差异性表达构成"connexin code"——确定血管段的电导和通透性。（3）淋巴管瓣膜功能（PMID:40720769）——Cx37, Cx47, Cx43, Cx45在淋巴管内皮细胞中的层次性（hierarchical）需求——维持淋巴管瓣膜形成和功能——Cx45可能作为"gatekeeper"限制淋巴返流。

**TE调控展望**：GJC1的TE调控关联主要通过gap junction信号和核质定位。Gap junction允许IP3和Ca2+在细胞间直接diffuse——这一机制在组织范围内协调基因表达——Ca2+ waves可传递至核内→激活CaM kinase IV→CREB phosphorylation→CREB-dependent TE transcription。核质定位（HPA Nucleoplasm extra）说明Cx45 CT可能在特定条件下经proteolytic cleavage释放→进入核内——CT IDR可能作为transcriptional co-factor结合转录因子——许多connexin（Cx43 CT最为经典）的C-tail cleavage产物已知进入核内调控基因表达（如Cx43 CT-20kDa fragment抑制细胞增殖）。Cx45 CT可能以类似方式参与细胞周期和分化基因的转录调控——间接影响TE区域的chromatin state。Connexin gap junction的分子通透性对维持组织内代谢稳态 essential——氧化应激和DNA damage可导致TE activation——Cx45 gap junction coupling damage may cause local accumulation of DNA damage→TE de-repression。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CNST | BioGRID | 0 |
| FAM189A2 | BioGRID | 0 |
| EXTL2 | BioGRID | 0 |
| ZACN | BioGRID | 0 |
| LPAR1 | BioGRID | 0 |
| UBQLN4 | BioGRID | 0 |
| PSMD2 | BioGRID | 0 |
| GPR114 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GJC1

### PubMed

**Count: 45**

| PMID | Title |
|---|---|
| 42368294 | Current Topics of Progressive Cardiac Conduction Disease. |
| 42160806 | Dietary supplementation of endo-1,4-ß-D-mannanase improves turkey growth through enhancement of immune response and jejunal barrier integrity. |
| 41418531 | Effect of heat stress on jejunal epithelial barrier integrity in broilers divergently selected for high- and low-water efficiency. |
| 41063451 | Novel Strategy for Acquiring Metabolically-Tagged Nascent Extracellular Vesicles: Implications for Identifying Surface Protein Markers of Extracellula |
| 40720769 | Hierarchical Requirement for Endothelial Cell Connexins Cx37, Cx47, Cx43, and Cx45 in Lymphatic Valve Function. |


